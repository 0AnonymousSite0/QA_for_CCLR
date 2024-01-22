import openai
import os
#openai.api_key="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"
#openai.api_base="https://ngapi.fun"
#openai.organization="org-G1BZDUMG5VO1kBA4GlNAxgFc"
#openai_api_key="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"
#openai_api_key="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"

os.environ["OPENAI_API_KEY"] = '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'
import pandas as pd
import re
import os
import csv
from bs4 import BeautifulSoup
import pandas as pd
#from docx import Document
import uuid
import pandas as pd
import openpyxl
from llama_index.embeddings import OpenAIEmbedding
from llama_index import GPTVectorStoreIndex, download_loader
from pathlib import Path
from llama_index import download_loader
from llama_index import (GPTKeywordTableIndex,SimpleDirectoryReader,LLMPredictor, ServiceContext)
from llama_index import download_loader
from langchain import OpenAI
from llama_index import StorageContext, load_index_from_storage
import numpy as np

GraphDBCypherReader = download_loader('GraphDBCypherReader')
llm_predictor1 = LLMPredictor(llm=OpenAI(temperature=0,top_p=0,model_name="text-davinci-003"))
llm_predictor2 = LLMPredictor(llm=OpenAI(temperature=0, top_p=0,model_name="gpt-3.5-turbo"))
llm_predictor3 = LLMPredictor(llm=OpenAI(temperature=0, top_p=0,model_name="gpt-4"))
service_context1 = ServiceContext.from_defaults(llm_predictor=llm_predictor1)
service_context2 = ServiceContext.from_defaults(llm_predictor=llm_predictor2)
service_context3 = ServiceContext.from_defaults(llm_predictor=llm_predictor3)

storage_context = StorageContext.from_defaults(persist_dir="./storage_of_KG")
index2 = load_index_from_storage(storage_context)
index1 = load_index_from_storage(storage_context)
index3 = load_index_from_storage(storage_context)

print("Knowledge Graph loaded")
def score_of_single_choice(answers_from_model, correct_answer):
  score = 0
  number_of_answers=0
  if correct_answer in str(answers_from_model):
    score = 1
  if "A" in correct_answer:
    number_of_answers=number_of_answers+1
  if "B" in correct_answer:
    number_of_answers=number_of_answers+1
  if "C" in correct_answer:
    number_of_answers=number_of_answers+1
  if "D" in correct_answer:
    number_of_answers=number_of_answers+1
  if number_of_answers>1:
    score=0
  return score
def save_df_to_excel(df, file_path, sheet_name):
  writer = pd.ExcelWriter(file_path)


  df.to_excel(writer, sheet_name=sheet_name, index=False)


  writer.close()
def split_correct_answers(string):
  answer = []
  for character in string:
    answer.append(character)
  return answer
def score_of_multi_choice(answers_from_model, correct_answers):
  score = 0
  correct_ones = 0
  missed_ones = 0
  wrong_ones = 0
  individual_correct_answers = split_correct_answers(correct_answers)
  for individual_answer in individual_correct_answers:
    if individual_answer in str(answers_from_model):
      correct_ones = correct_ones + 1
    if individual_answer not in str(answers_from_model):
      missed_ones = missed_ones + 1
  wrong_answers = set(["A", "B", "C", "D", "E"]).difference(correct_answers)
  for individual_wrong_answer in wrong_answers:
    if individual_wrong_answer in str(answers_from_model):
      wrong_ones = wrong_ones + 1

  if wrong_ones == 0:
    if missed_ones == 0:
      score = 2
    else:
      score = min(correct_ones * 0.5, 2)
  return score
def read_excel_column(file_path, sheet_name, column_name):
  df = pd.read_excel(file_path, sheet_name=sheet_name)

  column_data = df[column_name].tolist()

  return column_data
def final_score(Question, answers_from_model, answers):
  if "四个" in Question:
    score = score_of_single_choice(answers_from_model, answers)
  if "五个" in Question:
    score = score_of_multi_choice(answers_from_model, answers)
  return score
years=["First_Level_in_RCQE_2014"]

queryEngine1 = index2.as_query_engine(service_context=service_context1)
queryEngine2 = index2.as_query_engine(service_context=service_context2)
queryEngine3 = index2.as_query_engine(service_context=service_context3)

for year in years:
  print("Code of the Examination",year)
  Questions=read_excel_column(year+".xlsx", "Sheet1", "问题")
  Answers=read_excel_column(year+".xlsx", "Sheet1", "correct1")
  df = pd.DataFrame(columns=["Question","Correct_Answer",'Answer1', "Score1","Answer2","Score2","Answer3","Score3"])
  for i in range(len(Questions)):
    print(Questions[i])
    answer2 = queryEngine2.query(Questions[i])
    answer1 = queryEngine1.query(Questions[i])
    answer3 = queryEngine3.query(Questions[i])
    df2 = pd.DataFrame([{"Question":Questions[i],"Correct_Answer":Answers[i],"Answer1":answer1,"Score1":final_score(Questions[i],answer1,Answers[i]),"Answer2":answer2,"Score2":final_score(Questions[i],answer2,Answers[i]),"Answer3":answer3,"Score3":final_score(Questions[i],answer3,Answers[i])}])
    print("No of Question",i+1,"\n","Right_Answer:",Answers[i],"\n"+"Answer_from_text_davinci_003:",str(answer1).strip().replace("\n",""),"\nAnswer_from_:GPT3.5Turbo",str(answer2).strip().replace("\n",""),"\nAnswer_from_GPT4:",str(answer3).strip().replace("\n",""))
    df = pd.concat([df, df2], axis=0)
  save_df_to_excel(df, "All_answers_from_text-davinci-003_GPT-3.5_GPT-4_with_KG"+year+".xlsx", "sheet1")



