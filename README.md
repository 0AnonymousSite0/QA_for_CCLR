# Integrating Domain-Specific Knowledge Graph with Large Language Model for Question-Answering of Construction Laws and Regulations: A Case of Chinese Registered Constructor Qualification Examination

## !!! As the paper is under review, all contents in this repository currently are not allowed to be re-used by anyone until this announcement is deleted.

# 0. The inventory of all materials in this Github repository

# 1. General Introduction

## 1.1 This repository aims at providing the codes and data regarding the paper entitled “……” for the public, and it is developed by University of XXX in UK,  The University of XX in Hong Kong SAR, and XXX University in China.

## 1.2 We greatly appreciate the selfless spirits of these voluntary contributors of a series of open python libraries, including Bert (https://github.com/google-research/bert), Tensorflow (https://github.com/tensorflow/models), pytorch (https://github.com/pytorch/pytorch), Keras (https://github.com/keras-team/keras), Numpy (https://numpy.org/), labelImg (https://github.com/tzutalin/labelImg), pyExcelerator (https://github.com/WoLpH/pyExcelerator), some base works (https://github.com/yongzhuo/Keras-TextClassification, https://github.com/zjunlp/DeepKE/tree/master), and so on. Our work stands on the shoulders of these giants.

## 1.3 As for anything regarding the copyright, please refer to the MIT License or contact the authors.

# 2. Summary of supplemental materials

This table below shows all supplemental materials. All sheets in Tables S1, S2, and S3 are arranged in the order shown in this table.

![Inventory of supplemental materials.png](https://s2.loli.net/2024/01/22/F6fcy3kaARv8hzM.png)

All supplemental materials including shared codes， testing dataset, and developed Chinese Construction Laws and Regulations are available in the GitHub repository(https://github.com/0AnonymousSite0/shenghuazhou-QA_for_Chinese_Construction_Laws_and_Regulations)

# 3. Ranking List

The test results of different large language models on the QA dataset for Chinese Construction Laws and Regulations are shown below. It is worth noting that these models are evaluated based on a qualification rate of 0.6.

| Large Language Model | Publishing Institution | Overall Scoring Rate | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | Ranking |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|------|------|
| ERNIE-Bot 4.0 with knowledge graph | 百度智能云 | 0.823 | 0.842 | 0.826 | 0.830 | 0.801 | 0.853 | 0.842 | 0.800 | 0.862 | 1 |
| ERNIE-Bot 4.0 | 百度智能云 | 0.757 | 0.783 | 0.718 | 0.762 | 0.768 | 0.724 | 0.724 | 0.731 | 0.788 | 2 |
| GPT-4 with knowledge graph | OpenAI | 0.666 | 0.719 | 0.734 | 0.661 | 0.660 | 0.757 | 0.681 | 0.664 | 0.689 | 3 |
| GPT-4 | OpenAI | 0.532 | 0.602 | 0.490 | 0.556 | 0.536 | 0.570 | 0.519 | 0.514 | 0.566 | 4 |
| GPT-3.5-turbo with knowledge graph | OpenAI | 0.504 | 0.532 | 0.503 | 0.527 | 0.472 | 0.626 | 0.522 | 0.540 | 0.467 | 5 |
| ChatGLM3-6B with knowledge graph | Tsinghua & Zhipu.AI | 0.483 | 0.497 | 0.444 | 0.510 | 0.421 | 0.540 | 0.596 | 0.543 | 0.444 | 6 |
| Text-davinci-003 with knowledge graph | OpenAI | 0.482 | 0.507 | 0.521 | 0.470 | 0.478 | 0.582 | 0.516 | 0.510 | 0.516 | 7 |
| Qianfan-Chinese-Llama-2-7B with knowledge graph| 百度智能云 | 0.474 | 0.474 | 0.486 | 0.494 | 0.469 | 0.570 | 0.529 | 0.514 | 0.470 | 8 |
| ChatGLM2-6B with knowledge graph | Tsinghua & Zhipu.AI | 0.472 | 0.471 | 0.469 | 0.488 | 0.464 | 0.517 | 0.507 | 0.528 | 0.462 | 9 |
| ChatGLM2-6B | Tsinghua & Zhipu.AI | 0.430 | 0.454 | 0.412 | 0.477 | 0.409 | 0.469 | 0.444 | 0.494 | 0.420 | 10 |
| ChatGLM3-6B | Tsinghua & Zhipu.AI | 0.399 | 0.452 | 0.389 | 0.415 | 0.356 | 0.412 | 0.389 | 0.416 | 0.399 | 11 |
| Qianfan-Chinese-Llama-2-7B | 百度智能云 | 0.373 | 0.421 | 0.377 | 0.364 | 0.359 | 0.422 | 0.374 | 0.411 | 0.358 | 12 |
| GPT-3.5-turbo | OpenAI | 0.348 | 0.422 | 0.317 | 0.368 | 0.322 | 0.438 | 0.332 | 0.405 | 0.333 | 13 |
| Llama-2-70b with knowledge graph | MetaAI | 0.377 | 0.335 | 0.369 | 0.323 | 0.328 | 0.414 | 0.354 | 0.335 | 0.332 | 14 |
| Text-davinci-003 | OpenAI | 0.328 | 0.351 | 0.318 | 0.343 | 0.334 | 0.382 | 0.343 | 0.361 | 0.341 | 15 |
| Llama-2-70b | MetaAI | 0.284 | 0.284 | 0.338 | 0.255 | 0.316 | 0.313 | 0.291 | 0.299 | 0.293 | 16 |

# 4. Repository reuse
## 4.1 Set environment 
All codes are developed on Python 3.9, and the IDE adopted is PyCharm (Professional version). The codes also support GPU computing for higher speed; the Navida CUDA we adopted is V10.0.130. The GIS platform is Arcgis Pro 2.3, and its license is necessary. 

aiohttp==3.9.0

aiolimiter==1.1.0

aiosignal==1.3.1

aiostream==0.5.2

annotated-types==0.6.0

anyio==3.7.1

async-timeout==4.0.3

attrs==23.1.0

backoff==2.2.1

bce-python-sdk==0.8.96

bcrypt==4.0.1

beautifulsoup4==4.12.2

bs4==0.0.1

cachetools==5.3.2

certifi==2023.11.17

chardet==5.2.0

charset-normalizer==3.3.2

chroma-hnswlib==0.7.3

chromadb==0.4.17

click==8.1.7

colorama==0.4.6

coloredlogs==15.0.1

dataclasses-json==0.5.14

Deprecated==1.2.14

distro==1.8.0

emoji==2.8.0

et-xmlfile==1.1.0

exceptiongroup==1.1.3

fastapi==0.104.1

filelock==3.13.1

filetype==1.2.0

flatbuffers==23.5.26

frozenlist==1.4.0

fsspec==2023.10.0

future==0.18.3

google-auth==2.23.4

googleapis-common-protos==1.61.0

greenlet==3.0.1

grpcio==1.59.3

h11==0.14.0

httpcore==1.0.2

httptools==0.6.1

httpx==0.25.1

huggingface-hub==0.19.4

humanfriendly==10.0

idna==3.4

importlib-metadata==6.8.0

importlib-resources==6.1.1

install==1.3.5

joblib==1.3.2

jsonpatch==1.33

jsonpointer==2.4

kubernetes==28.1.0

langchain==0.0.338

langdetect==1.0.9

langsmith==0.0.65

llama-index==0.9.4

lxml==4.9.3

marshmallow==3.20.1

monotonic==1.6

mpmath==1.3.0

multidict==6.0.4

mypy-extensions==1.0.0

neo4j==5.14.1

nest-asyncio==1.5.8

networkx==3.2.1

nltk==3.8.1

numpy==1.26.2

oauthlib==3.2.2

onnxruntime==1.16.2

openai==1.3.3

openpyxl==3.1.2

opentelemetry-api==1.21.0

opentelemetry-exporter-otlp-proto-common==1.21.0

opentelemetry-exporter-otlp-proto-grpc==1.21.0

opentelemetry-proto==1.21.0

opentelemetry-sdk==1.21.0

opentelemetry-semantic-conventions==0.42b0

overrides==7.4.0

packaging==23.2

pandas==2.1.3

posthog==3.0.2

protobuf==4.25.1

pulsar-client==3.3.0

pyarrow==14.0.1

pyasn1==0.5.0

pyasn1-modules==0.3.0

pycryptodome==3.19.0

pydantic==2.5.1

pydantic-settings==2.1.0

pydantic_core==2.14.3

PyPika==0.48.9

pyreadline3==3.4.1

python-dateutil==2.8.2

python-docx==1.1.0

python-dotenv==1.0.0

python-iso639==2023.6.15

python-magic==0.4.27

pytz==2023.3.post1

PyYAML==6.0.1

qianfan==0.1.4

rapidfuzz==3.5.2

regex==2023.10.3

requests==2.31.0

requests-oauthlib==1.3.1

rsa==4.9

six==1.16.0

sniffio==1.3.0

soupsieve==2.5

SQLAlchemy==2.0.23

starlette==0.27.0

sympy==1.12

tabulate==0.9.0

tenacity==8.2.3

tiktoken==0.5.1

tokenizers==0.15.0

tqdm==4.66.1

typer==0.9.0

typing-inspect==0.9.0

typing_extensions==4.8.0

tzdata==2023.3

unstructured==0.10.30

urllib3==1.26.18

uvicorn==0.24.0.post1

watchfiles==0.21.0

websocket-client==1.6.4

websockets==12.0

wrapt==1.16.0

yarl==1.9.2

zipp==3.17.0

Before submitting these codes to Github, all of them have been tested to be well-performed (as shown in the screenshots). Even so, we are not able to guarantee their operation in other computing environments due to the differences in the Python version, computer operating system, and adopted hardware.

## 4.2 Testing the models
### 4.2.1 chroma-formatted vectorized CCLR knowledge graph
The data layer development in CCLR knowledge graph includes determining the three-tier knowledge domain framework, collecting and iteratively refining the laws and regulations, and dividing each law or regulation into multiple clauses.

![the first layer of knowledge graph.png](https://s2.loli.net/2024/01/22/7498MLCUmz5FuyN.png)

↑↑↑The first layer of knowledge graph

![the second layer of knowledge graph.png](https://s2.loli.net/2024/01/22/fTV95qJgUuEMNm6.png)

↑↑↑The second layer of knowledge graph

![the third layer of knowledge graph.png](https://s2.loli.net/2024/01/22/2v8ranX3DqUVY4T.png)

↑↑↑The third layer of knowledge graph

### 4.2.2 Codes for testing the models
Closed-source LLMs are API-only, while open-source LLMs over 24GB also use APIs to avoid high-end GPU costs. The open-source LLMs under 24GB are deployed directly on the AutoDL Cloud server with GTX 4090 GPUs.

![original LLMs目录截图.png](https://s2.loli.net/2024/01/22/fVB48XQCJWKz9x5.png)

↑↑↑Codes for testing original large language models

![LLMs with KG 目录截图.png](https://s2.loli.net/2024/01/22/2I9iHBQl1xSWtAV.png)

↑↑↑Codes for testing large language models integrating knowledge graph

![GIF for running video of original LLMs.gif](https://s2.loli.net/2024/01/22/SrCTb8xwA6KsFau.gif)
↑↑↑Multiple original LLMs simultaneously answering the CLLR-related questions

![GIF for running video of original LLMs.gif](https://s2.loli.net/2024/01/22/9gDGrmlRIMBxqc4.gif)
↑↑↑Multiple LLMs with knowledge graph simultaneously answering the CLLR-related questions
