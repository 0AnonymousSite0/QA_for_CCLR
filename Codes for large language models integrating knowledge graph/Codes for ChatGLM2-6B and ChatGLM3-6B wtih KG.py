from configs.model_config import *
from chains.local_doc_qa import LocalDocQA
import os
import nltk
from models.loader.args import parser
import models.shared as shared
from models.loader import LoaderCheckPoint
nltk.data.path = [NLTK_DATA_PATH] + nltk.data.path
from transformers import AutoTokenizer, AutoModel
import os

# Show reply with source text from input document
REPLY_WITH_SOURCE = True

messages = []
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

def save_df_to_excel(df, file_path, sheet_name):
  writer = pd.ExcelWriter(file_path)

  df.to_excel(writer, sheet_name=sheet_name, index=False)


  writer.close()
    
    
def split_correct_answers(string):
  answer = []
  for character in string:
    answer.append(character)
  return answer


def read_excel_column(file_path, sheet_name, column_name):
  df = pd.read_excel(file_path, sheet_name=sheet_name)

  column_data = df[column_name].tolist()

  return column_data


def get_file_names(folder):

     file_names = [str(folder)+r"/"+filename for filename in os.listdir(folder) if os.path.isfile(os.path.join(folder, filename))]

     file_name_str = ",".join(file_names)
    
     return file_name_str




def main():

    llm_model_ins = shared.loaderLLM()
    llm_model_ins.history_len = LLM_HISTORY_LEN

    local_doc_qa = LocalDocQA()
    local_doc_qa.init_cfg(llm_model=llm_model_ins,
                          embedding_model=EMBEDDING_MODEL,
                          embedding_device=EMBEDDING_DEVICE,
                          top_k=VECTOR_SEARCH_TOP_K)
        # vs_path = None
    # while not vs_path:
    #filepath=get_file_names(r"/root/autodl-tmp/langchain-ChatGLM/KG")
    filepath=get_file_names(r"/root/autodl-tmp/langchain-ChatGLM/allfiles_docx0823")
    #filepath=get_file_names(r"/root/autodl-tmp/langchain-ChatGLM/KG_doc")
    

    print(filepath)

    filepath = filepath.split(",")

    temp,loaded_files = local_doc_qa.init_knowledge_vector_store(filepath)
    if temp is not None:
        vs_path = temp

    years=["First_Level_in_RCQE_2014"]
    

    for year in years:
        print("Code of the examination",year)
        Questions=read_excel_column(year+".xlsx", "Sheet1", "信息")
        Answers=read_excel_column(year+".xlsx", "Sheet1", "法律依据")
        df = pd.DataFrame(columns=["Question","Correct_Answer",'Answer1', "Answer2", "Answer3"])

        
        for i in range(len(Questions)):
            query=Questions[i]
            answers_from_model = local_doc_qa.get_knowledge_based_answer(query=query,
                                                                         vs_path=vs_path,
                                                                         chat_history=[],
                                                                         streaming=False)
            answers_from_model=list(answers_from_model)
            answers_from_model=answers_from_model[0]
            answers_from_model=answers_from_model[0]["result"]
            print(answers_from_model)
            answer1=list(answers_from_model)
            answer2="1"
            answer3="1"
            
            df2 = pd.DataFrame([{"Question":Questions[i],"Correct_Answer":Answers[i],"Answer1":answer1,"Answer2":answer2,"Answer3":answer3}])
            print("No Question",i+1,"\n","Right_Answer:",Answers[i],"\nAnswer_fromm_fine-tuned_Chatglm2_6B_with_domain_knowledge:",str(answer1).strip().replace("\n",""))
            df = pd.concat([df, df2], axis=0)

        save_df_to_excel(df, "All_answers_from_ChatGLM3_6B_with_KG"+year+".xlsx", "sheet1")


        
