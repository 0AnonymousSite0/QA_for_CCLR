# Integrating Domain-Specific Knowledge Graph with Large Language Model for Question-Answering of Construction Laws and Regulations

## !!! As the paper is under work, all contents in this repository currently are not allowed to be re-used by anyone until this announcement is deleted.

# 0. Videos of running the LLMs before and after integrating the CCLR knowledge graph
![GIF for running video of original LLMs.gif](https://s2.loli.net/2024/01/22/SrCTb8xwA6KsFau.gif)
↑↑↑Multiple original LLMs simultaneously answering the CLLR-related questions

![GIF for running video of original LLMs.gif](https://s2.loli.net/2024/01/22/9gDGrmlRIMBxqc4.gif)
↑↑↑Multiple LLMs with knowledge graph simultaneously answering the CLLR-related questions


# The inventory of all materials in this Github repository

# 1. General Introduction

1.1 This repository aims at providing the codes and data regarding the paper entitled “……” for the public, and it is developed by University of XXX in UK,  The University of XX in Hong Kong SAR, and XXX University in China.

1.2 We greatly appreciate the selfless spirits of these voluntary contributors of a series of open python libraries, including Bert (https://github.com/google-research/bert), Tensorflow (https://github.com/tensorflow/models), pytorch (https://github.com/pytorch/pytorch), Keras (https://github.com/keras-team/keras), Numpy (https://numpy.org/), labelImg (https://github.com/tzutalin/labelImg), pyExcelerator (https://github.com/WoLpH/pyExcelerator), some base works (https://github.com/yongzhuo/Keras-TextClassification, https://github.com/zjunlp/DeepKE/tree/master), and so on. Our work stands on the shoulders of these giants.

1.3 As for anything regarding the copyright, please refer to the MIT License or contact the authors.

# 2. Summary of supplemental materials

The table below shows all supplemental materials. All sheets in Tables S1, S2, S3, and S4 are arranged in the order shown in this table.

![Inventory of supplemental materials.png](https://s2.loli.net/2024/02/02/Pb8QhOYeawlDE1k.png)

All supplemental materials including shared codes, testing dataset, and developed Chinese Construction Laws and Regulations are available in the GitHub repository(https://github.com/0AnonymousSite0/shenghuazhou-QA_for_Chinese_Construction_Laws_and_Regulations)

# 3. LLM Leaderboard for CCLR QA

The test results of different large language models on the QA dataset for Chinese Construction Laws and Regulations are shown below.

| Large Language Model | Publishing Institution | Overall Scoring Rate | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | Ranking |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|------|------|
| ERNIE-Bot 4.0 with knowledge graph | Baidu&The authors | 0.822 | 0.842 | 0.826 | 0.830 | 0.801 | 0.853 | 0.842 | 0.800 | 0.862 | 1 |
| ERNIE-Bot 4.0 | Baidu | 0.757 | 0.783 | 0.718 | 0.762 | 0.768 | 0.724 | 0.724 | 0.731 | 0.788 | 2 |
| GPT-4 with knowledge graph | OpenAI&The authors | 0.666 | 0.719 | 0.734 | 0.661 | 0.660 | 0.757 | 0.681 | 0.664 | 0.689 | 3 |
| GPT-4 | OpenAI | 0.532 | 0.602 | 0.490 | 0.556 | 0.536 | 0.570 | 0.519 | 0.514 | 0.566 | 4 |
| GPT-3.5-turbo with knowledge graph | OpenAI&The authors | 0.504 | 0.532 | 0.503 | 0.527 | 0.472 | 0.626 | 0.522 | 0.540 | 0.467 | 5 |
| ChatGLM3-6B with knowledge graph | Tsinghua & Zhipu.AI | 0.483 | 0.497 | 0.444 | 0.510 | 0.421 | 0.540 | 0.596 | 0.543 | 0.444 | 6 |
| Text-davinci-003 with knowledge graph | OpenAI&The authors | 0.482 | 0.507 | 0.521 | 0.470 | 0.478 | 0.582 | 0.516 | 0.510 | 0.516 | 7 |
| Qianfan-Chinese-Llama-2-7B with knowledge graph| Baidu&The authors | 0.474 | 0.474 | 0.486 | 0.494 | 0.469 | 0.570 | 0.529 | 0.514 | 0.470 | 8 |
| ChatGLM2-6B with knowledge graph | Tsinghua & Zhipu.AI | 0.472 | 0.471 | 0.469 | 0.488 | 0.464 | 0.517 | 0.507 | 0.528 | 0.462 | 9 |
| ChatGLM2-6B | Tsinghua & Zhipu.AI | 0.430 | 0.454 | 0.412 | 0.477 | 0.409 | 0.469 | 0.444 | 0.494 | 0.420 | 10 |
| ChatGLM3-6B | Tsinghua & Zhipu.AI | 0.399 | 0.452 | 0.389 | 0.415 | 0.356 | 0.412 | 0.389 | 0.416 | 0.399 | 11 |
| Qianfan-Chinese-Llama-2-7B | Baidu | 0.373 | 0.421 | 0.377 | 0.364 | 0.359 | 0.422 | 0.374 | 0.411 | 0.358 | 12 |
| GPT-3.5-turbo | OpenAI | 0.348 | 0.422 | 0.317 | 0.368 | 0.322 | 0.438 | 0.332 | 0.405 | 0.333 | 13 |
| Llama-2-70b with knowledge graph | MetaAI&The authors | 0.377 | 0.335 | 0.369 | 0.323 | 0.328 | 0.414 | 0.354 | 0.335 | 0.332 | 14 |
| Text-davinci-003 | OpenAI | 0.328 | 0.351 | 0.318 | 0.343 | 0.334 | 0.382 | 0.343 | 0.361 | 0.341 | 15 |
| Llama-2-70b | MetaAI | 0.284 | 0.284 | 0.338 | 0.255 | 0.316 | 0.313 | 0.291 | 0.299 | 0.293 | 16 |

# 4. CCLR knowledge graph development

## 4.1 CCLR knowledge graph download

![CCLR knowledge graph.png](https://s2.loli.net/2024/02/02/VXl7TG5KRdsU4cI.png)

The CCLR knowledge graph is available through this link (https://drive.google.com/drive/folders/1G0mTvOg7cYZAXUC9VmPsPHuqZ1DpZH55?usp=sharing).

## 4.2 Data layer development of CCLR knowledge graph

The data layer development in the CCLR knowledge graph includes determining the three-tier knowledge domain framework, collecting and iteratively refining the laws and regulations, and dividing each law or regulation into multiple clauses.

![Fig. S1 The first layer of the knowledge graph.png](https://s2.loli.net/2024/02/02/926XPw7pKF1xGi4.png)

↑↑↑The first data layer of the knowledge graph

![Fig. S2.png](https://s2.loli.net/2024/02/02/ekjHbGnOrcEPMzt.png)

↑↑↑The second data layer of the knowledge graph

![Fig. S3.png](https://s2.loli.net/2024/02/02/yV4x5z2kwESihoe.png)

↑↑↑The third data layer of the knowledge graph

# 5. Test dataset development

Our dataset is specifically tailored to the CCLR domain and encompasses 6,339 questions while other notable datasets such as c-eval typically consist of approximately 500 questions within a singular domain.

![QA_dataset in huggingface.png](https://s2.loli.net/2024/02/02/QSdy7GnkHYoUz51.png)

↑↑↑The QA dataset in huggingface

![A example of one single-answer and multi-answer question in CCLR QA dataset.png](https://s2.loli.net/2024/02/02/o8raWi4hHUOC6mf.png)

↑↑↑The examples of one single-answer and multi-answer question in the CCLR QA dataset

More information about the dataset can be found through this link (https://huggingface.co/datasets/AnonymousSite/QA_dataset_for_CCLR).

# 6. Repository reuse

## 6.1 Environment set

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

......

Please refer to the supplementary materials for the complete requirement file.(https://github.com/0AnonymousSite0/QA_for_CCLR/blob/main/Codes/Codes%20for%20large%20language%20models%20integrating%20knowledge%20graph/requirements.txt)

Before submitting these codes to Github, all of them have been tested to be well-performed (as shown in the screenshots). Even so, we are not able to guarantee their operation in other computing environments due to the differences in the Python version, computer operating system, and adopted hardware.

## 6.2 Codes for testing the LLMs

Closed-source LLMs are API-only, while open-source LLMs over 24GB also use APIs to avoid high-end GPU costs. The open-source LLMs under 24GB are deployed directly on the AutoDL Cloud server with GTX 4090 GPUs.

![original LLMs目录截图.png](https://s2.loli.net/2024/01/22/fVB48XQCJWKz9x5.png)

↑↑↑Codes for testing original large language models

![LLMs with KG 目录截图.png](https://s2.loli.net/2024/01/22/2I9iHBQl1xSWtAV.png)

↑↑↑Codes for testing large language models integrating knowledge graph



