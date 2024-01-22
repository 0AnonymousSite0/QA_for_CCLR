# Integrating Domain-Specific Knowledge Graph with Large Language Model for Question-Answering of Construction Laws and Regulations: A Case of Chinese Registered Constructor Qualification Examination

## !!! As the paper is under review, all contents in this repository currently are not allowed to be re-used by anyone until this announcement is deleted.

# 0. The inventory of all materials in this Github repository

# 1. General Introduction

1.1 This repository aims at providing the codes and data regarding the paper entitled “……” for the public, and it is developed by University of XXX in UK,  The University of XX in Hong Kong SAR, and XXX University in China.

1.2 We greatly appreciate the selfless spirits of these voluntary contributors of a series of open python libraries, including Bert (https://github.com/google-research/bert), Tensorflow (https://github.com/tensorflow/models), pytorch (https://github.com/pytorch/pytorch), Keras (https://github.com/keras-team/keras), Numpy (https://numpy.org/), labelImg (https://github.com/tzutalin/labelImg), pyExcelerator (https://github.com/WoLpH/pyExcelerator), some base works (https://github.com/yongzhuo/Keras-TextClassification, https://github.com/zjunlp/DeepKE/tree/master), and so on. Our work stands on the shoulders of these giants.

1.3 As for anything regarding the copyright, please refer to the MIT License or contact the authors.

# 2. Ranking List

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




# 3. Summary of supplemental materials

This table below shows all supplemental materials. All sheets in Tables S1, S2, and S3 are arranged in the order shown in this table.



# 4. Repository reuse

