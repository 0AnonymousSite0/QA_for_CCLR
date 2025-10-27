# Integrating Domain-Specific Knowledge Graph with Large Language Model for Question-Answering (QA) of Construction Laws and Regulations

## !!! As the paper is under review, all materials in this repository currently are not allowed to be re-used by anyone until this announcement is deleted.

# 0. Videos of running the LLMs before and after integrating the CCLR knowledge graph
![GIF for running video of original LLMs.gif](https://s2.loli.net/2024/01/22/SrCTb8xwA6KsFau.gif)
↑↑↑Multiple original LLMs simultaneously answering the CLLR-related questions

![GIF for running video of original LLMs.gif](https://s2.loli.net/2024/01/22/9gDGrmlRIMBxqc4.gif)
↑↑↑Multiple LLMs with knowledge graph simultaneously answering the CLLR-related questions


# 1. General introduction of this repository

1.1 This repository aims at providing the codes and data regarding the paper entitled “……” for the public, and it is developed by University of XXX in UK,  The University of XX in Hong Kong SAR, and XXX University in China.

1.2 We greatly appreciate the selfless spirits of these voluntary contributors of a series of open python libraries, including langchain, llamaindex, meta's llama2, openai, chatglm, numpy, and so on. Our work stands on the shoulders of these giants.

1.3 As for anything regarding the copyright, please refer to the MIT License or contact the authors.

# 2. Summary of supplemental materials in this repository

The table below shows all supplemental materials. All sheets in Tables S1 to S10 are arranged in the order shown in this table.

![图片2.png](https://s2.loli.net/2025/10/27/gUxLCYMoyXzq2k5.png)

All supplemental materials are provided in Github repository (https://huggingface.co/datasets/AnonymousSite/QA_dataset_for_CCLR). Besides the Github repository, the  CCLR QA dataset is also shared in Hugging Face repository (https://github.com/0AnonymousSite0/QA_for_CCLR).

# 3. LLM Leaderboard for CCLR QA

The test results of different large language models on the QA dataset for Chinese Construction Laws and Regulations are shown below. Welcome global scholars to test their LLM works on CCLR QA, please see the following specification of reusing the QA dataset.

| Large Language Model | Contributors | Overall Scoring Rate | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | Ranking |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|------|------|
| ERNIE-Bot 4.0 with knowledge graph | Baidu & The authors | 0.830 | 0.847 | 0.862 | 0.847 | 0.821 | 0.856 | 0.836 | 0.783 | 0.838 | 1 |
| ERNIE-Bot 4.0 | Baidu | 0.761 | 0.795 | 0.736 | 0.751 | 0.788 | 0.719 | 0.698 | 0.717 | 0.772 | 2 |
| GPT-4 with knowledge graph | OpenAI & The authors | 0.659 | 0.745 | 0.762 | 0.672 | 0.697 | 0.799 | 0.702 | 0.671 | 0.671 | 3 |
| GPT-4 | OpenAI | 0.528 | 0.633 | 0.496 | 0.566 | 0.585 | 0.574 | 0.513 | 0.532 | 0.563 | 4 |
| GPT-3.5-turbo with knowledge graph | OpenAI & The authors | 0.498 | 0.553 | 0.585 | 0.530 | 0.478 | 0.645 | 0.536 | 0.541 | 0.451 | 5 |
| ChatGLM2-6B with knowledge graph | Tsinghua, Zhipu.AI & The authors | 0.464 | 0.485 | 0.509 | 0.471 | 0.491 | 0.523 | 0.515 | 0.543 | 0.464 | 6 |
| Qianfan-Chinese-Llama-2-7B with knowledge graph| Baidu & The authors | 0.462 | 0.489 | 0.517 | 0.502 | 0.498 | 0.561 | 0.543 | 0.535 | 0.458 | 7 |
| ChatGLM3-6B with knowledge graph | Tsinghua, Zhipu.AI & The authors | 0.435 | 0.484 | 0.486 | 0.502 | 0.454 | 0.533 | 0.505 | 0.528 | 0.439 | 8 |
| ChatGLM2-6B | Tsinghua & Zhipu.AI | 0.424 | 0.468 | 0.467 | 0.452 | 0.443 | 0.470 | 0.442 | 0.505 | 0.437 | 9 |
| ChatGLM3-6B | Tsinghua & Zhipu.AI | 0.392 | 0.470 | 0.421 | 0.390 | 0.392 | 0.423 | 0.378 | 0.428 | 0.382 | 10 |
| Qianfan-Chinese-Llama-2-7B | Baidu | 0.363 | 0.433 | 0.376 | 0.374 | 0.377 | 0.447 | 0.369 | 0.452 | 0.355 | 11 |
| GPT-3.5-turbo | OpenAI | 0.351 | 0.440 | 0.325 | 0.368 | 0.364 | 0.462 | 0.350 | 0.413 | 0.347 | 12 |
| Llama-2-70b with knowledge graph | MetaAI & The authors | 0.335 | 0.323 | 0.381 | 0.354 | 0.328 | 0.373 | 0.349 | 0.344 | 0.321 | 13 |
| Llama-2-70b | MetaAI | 0.294 | 0.279 | 0.339 | 0.292 | 0.325 | 0.312 | 0.261 | 0.279 | 0.287 | 14 |

# 4. Reuse of the CCLR knowledge graph 

## 4.1 Three optional versions of CCLR knowledge graph

![CCLR knowledge graph.png](https://s2.loli.net/2024/02/02/VXl7TG5KRdsU4cI.png)

The CCLR knowledge graph is available through this link (https://drive.google.com/drive/folders/1G0mTvOg7cYZAXUC9VmPsPHuqZ1DpZH55?usp=sharing).

## 4.2 Data layer details of CCLR knowledge graph

The data layer development in the CCLR knowledge graph includes determining the three-tier knowledge domain framework, collecting and iteratively refining the laws and regulations, and dividing each law or regulation into multiple clauses.

![Fig. S1 The first layer of the knowledge graph.png](https://s2.loli.net/2024/02/02/926XPw7pKF1xGi4.png)

↑↑↑201 triples of [knowledge domain,, has subdomain of, knowledge domain]

![Fig. S2.png](https://s2.loli.net/2024/02/02/ekjHbGnOrcEPMzt.png)

↑↑↑657 triples of [knowledge domain, is related to, law and regulation]

![Fig. S3.png](https://s2.loli.net/2024/02/02/yV4x5z2kwESihoe.png)

↑↑↑2,213 triples of [law and regulation, contains, clause]

# 5. Reuse of the CCLR QA dataset

Our dataset is specifically tailored to the CCLR domain and encompasses 6,359 questions while other notable datasets such as c-eval typically consist of approximately 500 questions within a singular domain.

![QA_dataset in huggingface.png](https://s2.loli.net/2024/02/02/QSdy7GnkHYoUz51.png)

↑↑↑The QA dataset in huggingface

![A example of one single-answer and multi-answer question in CCLR QA dataset.png](https://s2.loli.net/2024/02/02/o8raWi4hHUOC6mf.png)

↑↑↑The examples of one single-answer and multi-answer question in the CCLR QA dataset

More information about the dataset can be found through this link (https://huggingface.co/datasets/AnonymousSite/QA_dataset_for_CCLR).

# 6. Reuse of the codes for running LLMs with and without CCLR knowledge graph
 
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






