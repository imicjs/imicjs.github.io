---
title: The paper of Wang Xiangxue’s research group from the IMIC laboratory was published in the internationally authoritative European Journal of Cancer
meta_title: The paper of Wang Xiangxue’s research group from the IMIC laboratory was published in the internationally authoritative European Journal of Cancer
description: Recently, the research group of Professor Wang Xiangxue of Jiangsu University Key Laboratory of Intelligent Medical Image Computing (IMIC) of Nanjing University of Information Science & Technology collaborated with multi-center teams such as Emory University and Fudan University Cancer Hospital in the United States to…
date: '2026-03-22T00:00:00+08:00'
image: /images/content/source-1505.jpg
categories:
- News
- Comprehensive news
author: IMIC Lab
tags:
- IMIC
- News
draft: false
source_url: https://imic.nuist.edu.cn/info/1032/1505.htm
translation_status: machine-translated-and-terminology-normalized
---

Recently, the research group of Professor Wang Xiangxue of Jiangsu University Key Laboratory of Intelligent Medical Image Computing (IMIC) of Nanjing University of Information Science & Technology collaborated with multi-center teams such as Emory University and Fudan University Cancer Hospital in the United States to publish the latest research results in the internationally authoritative journal "European Journal of Cancer" in the field of oncology (TOP of the First District of the Chinese Academy of Sciences).

The study is titled "MuTriM: A multiscale deep learning model integrating longitudinal radiomics and pathomic features for predicting recurrence and adjuvant radiation benefit in breast cancer". This research is dedicated to solving the core pain points of insufficient single-modality information and difficulty in capturing the spatio-temporal heterogeneity of tumors in breast cancer prognosis assessment. Based on routine clinical dynamic contrast-enhanced magnetic resonance imaging (DCE-MRI) and hematoxylin-eosin stained whole-slice images (WSI), a cross-modal and cross-time fusion deep learning model MuTriM based on the attention mechanism was innovatively constructed. The model (shown in Figure 1) achieves deep fusion of multi-scale features through a hierarchical architecture: on the pathological side, a self-supervised visual Transformer model is used to extract hierarchical pathomic features from single cells to tissue microenvironments from WSI, and a full-slice level morphological representation is generated through a self-attention mechanism; on the imaging side, longitudinal radiomic features are extracted from multiple enhancement phases of DCE-MRI, and the tumor blood perfusion and microvascular remodeling information reflected by the dynamic enhancement curve is encoded through a multi-layer perceptron. The core of the model adopts a cross-modal self-attention fusion mechanism, which not only realizes the interactive modeling of macroscopic image dynamics and microscopic cell morphology, but also realizes the joint capture of spatial cross-scale and time cross-sequence information within the same framework, and finally outputs a risk score for predicting recurrence-free survival (RFS) and the probability of benefit from adjuvant radiotherapy.

The model was trained in the Fudan University Cancer Hospital cohort (N=335) and externally validated in the TCGA public cohort (N=126). The results showed that the MuTriM model significantly predicted RFS (HR=5.26, C-index=0.75) in the subtype non-specific cohort, and its performance comprehensively surpassed the model based on a single modality. In addition, the MuTriM model showed the potential to guide radiotherapy decisions in the ER+ population: high-risk patients significantly benefited from adjuvant radiotherapy (HR=0.15, P=0.03), while low-risk patients did not see significant benefit (HR=4.06, P=0.53), and the interaction test was significant (P=0.04). Combined with transcriptome analysis, the study further revealed the immune escape and aggressive biological characteristics of high-risk tumors. This model provides strong support for precise risk stratification and personalized treatment decisions for breast cancer.

![The paper of Wang Xiangxue’s research group from the IMIC laboratory was published in the internationally authoritative European Journal of Cancer](/images/articles/source-1505/01.webp)

Figure 1. Schematic diagram of MuTriM model framework

Reference method and original link to this article

Xiangxue Wang, Liya Chen, Jingwen Sun, Sirvan Khalighi, Tanmoy Dam, Himanshu Maurya, Tilak Pathak, Cheng Lu, Shipra Gandhi, Sunil Badve, Shen Zhao, Wentao Yang, Jun Xu, Anant Madabhushi, Bolin Song, MuTriM: A multiscale deep learning model integrating longitudinal radiomics and pathomic features for predicting recurrence and adjuvant radiation benefit in breast cancer, European Journal of Cancer , vol. 238, 2026,116679. https://doi.org/10.1016/j.ejca.2026.116679

---

*Translated from the [original Chinese source](https://imic.nuist.edu.cn/info/1032/1505.htm).*
