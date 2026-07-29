---
title: The research results of Liu Mingxin, a doctoral student in the laboratory,
  were accepted by MICCAI2025, the top conference in the field of medical image computing.
date: '2025-06-19T00:00:00+08:00'
summary: 'The paper "Multimodal Representation Decoupling Network (MurreNet): Establishing
  an Integrated Multimodal Interaction Model between Histopathology and Genomic Atlas
  for Survival Prediction of Cancer Patients" by Liu Mingxin (supervisor: Professor
  Xu Jun), a doctoral student at Jiangsu University Key Laboratory of…'
type: blog
categories:
- Comprehensive news
tags:
- IMIC
- News·Notifications
source_url: https://imic.nuist.edu.cn/info/1032/1423.htm
source_language: zh-CN
translation_status: machine-translated-and-terminology-normalized
---

The paper "Multimodal Representation Decoupling Network (MurreNet): Establishing an Integrated Multimodal Interaction Model between Histopathology and Genomic Atlas for Survival Prediction of Cancer Patients" by Liu Mingxin (supervisor: Professor Xu Jun), a doctoral student at Jiangsu University Key Laboratory of Intelligent Medical Image Computing (IMIC), was officially accepted by the International Conference on Medical Image Computing and Computer Assisted Intervention (MICCAI 2025), the top conference in the field of medical image computing. This achievement is the latest innovative research result of IMIC laboratory in the field of computational pathology and multi-modal fusion, providing new solutions for cross-scale medical data: 1) pathology images and 2) multi-modal fusion of gene sequencing data and cancer survival prediction.

Research background

Cancer is one of the major diseases with a high mortality rate worldwide, and the assessment of patient survival prognosis plays an important role in clinical decision-making. Accurate survival prediction can not only help doctors formulate personalized treatment plans, but also provide patients with more scientific risk assessment and follow-up guidance. However, the high heterogeneity and complex pathological mechanisms of tumors pose great challenges to survival prediction. Traditional single-modality analysis methods, such as models based on clinical features or single molecular markers, often cannot fully reflect the multidimensional biological characteristics of tumors, limiting the accuracy and generalization ability of patient prognosis. Panoramic digital pathology slides (Whole-Slide Images, WSIs) use high-resolution imaging to display the structure at the cellular and tissue levels and their spatial interaction with the microenvironment from the perspective of tumor histology and morphology, which can reflect the macroscopic biological characteristics of tumors. At the same time, genomics technology provides a means to reveal the driving factors of tumors at the molecular level, including gene mutations, expression profiles and abnormal regulation of signaling pathways, reflecting the microscopic molecular status of tumors. The two reveal the intrinsic laws of cancer from different scales and perspectives and are highly complementary.

However, in clinical practice, these two types of data are usually processed in isolation, making it difficult to achieve effective fusion. WSIs data are huge and complex in structure, making it difficult for traditional image analysis to fully mine its potential prognostic information; while genomic data are high-dimensional and noisy, making biological interpretation difficult. How to design a scientific and reasonable multi-modal fusion strategy and effectively integrate morphological and molecular information has become the key to improving the accuracy of cancer survival prediction. In addition, there are complex correlations between tumor phenotypes and genotypes. Capturing this phenotype-genotype coupling relationship can not only deepen the understanding of tumor biological mechanisms, but also help to build more robust and interpretable prediction models. The main challenges facing current multi-modal fusion research include: significant differences in feature distribution between different modalities, and difficulty in distinguishing and extracting modal specificity and modal shared information; in addition, how to design effective interaction mechanisms to achieve complementation and enhancement of cross-modal information is also a bottleneck that needs to be broken through. Solving the above problems will promote the development of accurate survival prediction technology based on integrating pathological imaging and genomic data, and promote the optimization of clinical diagnosis and individualized treatment strategies.

research methods

In order to cope with the many challenges faced by current multi-modal survival prediction, we proposed the Multimodal Representation Decoupling Network (MurreNet), whose overall architecture is shown in Figure 1. This network is specifically designed to model the complex and profound interactive relationships between pathological images and genomic data, aiming to extract more comprehensive and hierarchical feature representations from multi-modal data to improve the accuracy and robustness of survival predictions. The core concept of MurreNet is to emphasize the decoupled learning of multi-modal representation, paying attention to the shared information between modalities and taking into account the specificity of each modality, thereby maximizing the utilization and optimal integration of information.

![The research results of Liu Mingxin, a doctoral student in the laboratory, were accepted by MICCAI2025, the top conference in the field of medical image computing.](https://imic.nuist.edu.cn/__local/2/E9/51/84FFCDE2A4D59395E8850513EDF_10DBF1DF_5DA94.png)

Figure 1: The multimodal representation decoupling network (MurreNet) model proposed in this paper includes the following four modules: (a) feature extraction module for pathological and genomic features, (b) multimodal representation decoupling module, (c) modal representation reconstruction module, (d) multimodal representation fusion through deep ensemble orthogonal fusion module, and comprehensive training regularization strategy for cancer prognosis.

Specifically, the contributions of this article are mainly reflected in the following three aspects:

1) The Multimodal Representation Decomposition (MRD) module is designed. This module uses a structured method to systematically distinguish between modal shared (common) and modal specific (specific) representations, allowing the model to capture the intrinsic characteristics of the two types of information respectively, avoiding the interference and information loss caused by the confusion of modal information in traditional methods, thereby providing a clearer and decoupled representation space for subsequent fusion.

2) Proposed the Deep Holistic Orthogonal Fusion (DHOF) module, which is based on the orthogonal constraint mechanism and effectively integrates modality sharing and modality-specific information to achieve deep fusion of complementary advantages. By maintaining the orthogonality of the two types of representations, DHOF not only promotes the effective transmission and integration of information, but also avoids the reuse of redundant information, improving the model's ability to express multi-modal complex relationships.

3) This paper introduces a comprehensive loss function combination, covering modal similarity, difference and reconstruction loss, forming a multiple constraint mechanism. This strategy not only promotes the consistency of shared information between modalities, but also strengthens the independent expression of modality-specific information, further guarantees the effective decoupling and complementary learning of multi-modal features, and provides a solid theoretical foundation and practical guidance for model training. Through extensive experimental verification on a large-scale cancer survival prediction data set, our method shows significant advantages over the current state-of-the-art multi-modal fusion strategies, fully demonstrating the excellent potential of MurreNet in capturing complex multi-modal interactions, improving prediction accuracy and clinical application value.

Experimental results

We selected six representative cancer types from The Cancer Genome Atlas (TCGA) to conduct systematic experiments, covering: Bladder Urothelial Carcinoma (BLCA), Breast Invasive Carcinoma (BRCA), Colorectal Adenocarcinoma (Colon & Rectum Adenocarcinoma, COADREAD), Lung Adenocarcinoma (Lung Adenocarcinoma, LUAD), endometrial cancer (Uterine Corpus Endometrial Carcinoma, UCEC), and gastric adenocarcinoma (Stomach Adenocarcinoma, STAD). In terms of genomic information modeling, we comprehensively utilize three types of core molecular data: RNA sequencing (RNA-seq), copy number variation (CNV), and gene mutation status. In order to further improve the biological explanation and structural expression of features, we reorganized these raw data by function and divided them into six key molecular subcategories: protein kinases, tumor suppressor genes, oncogenes, cell differentiation markers, transcription factors, and cytokines and growth factors. The above-mentioned multi-dimensional genomic subspaces together constitute the molecular representation input of the model, providing a solid foundation for in-depth characterization of the cross-modal association between pathological images and genetic features. The experimental results are shown in Table 1 below:

Table 1. Performance of different methods on six public TCGA datasets. “P.” indicates whether to use pathological images, and “G.” indicates whether to use genomic maps. The best and second best results are highlighted in red and blue respectively.

![The research results of Liu Mingxin, a doctoral student in the laboratory, were accepted by MICCAI2025, the top conference in the field of medical image computing.](https://imic.nuist.edu.cn/__local/C/7B/2F/089DAC80AA4F414C9BD9C6DE659_8EE33FEF_3DCD9.png)

To further verify the actual performance of our model in the survival analysis task, we divided all patients into high-risk and low-risk groups based on the median risk score predicted by the model in six TCGA cancer cohorts. Subsequently, as shown in Figure 2, this article uses the Kaplan-Meier survival curve to visually display the survival status of each group of patients and intuitively depict the time distribution trend of survival events. To assess the statistical significance of survival differences between groups, we used the log-rank test with a p value of 0.05 or less as the significance criterion. As shown in Figure 2, in six cancer types, our proposed MurreNet model all exhibits significant risk stratification capabilities, and its corresponding p-values ​​are all well below 0.05. This result fully proves the robustness and generalization ability of the model in individual prognosis prediction, and further confirms its broad application prospects in clinical risk assessment and precision medicine practice.

![The research results of Liu Mingxin, a doctoral student in the laboratory, were accepted by MICCAI2025, the top conference in the field of medical image computing.](https://imic.nuist.edu.cn/__local/3/EC/2E/0484A65E65E9B30D984E81C3045_13041086_9D0FF.png)

Figure 2. Kaplan-Meier survival curves of the proposed multimodal representation decoupled network (MurreNet) model on six cancer datasets

Conclusion

In this study, we propose an innovative multi-modal representation decoupling framework (MurreNet) designed to fuse genomic data with pathological whole-slice images (WSIs) to improve the survival prediction performance of cancer patients. The core of this framework lies in the Multimodal Representation Decomposition module (MRD) we designed, which can systematically decompose multimodal information into modality-common and modality-specific features, thereby achieving more refined and structured modal knowledge modeling. In order to enhance the constraints and generalization capabilities of model training, we introduced a combination of multiple losses, including modal similarity loss, modal difference loss, reconstruction loss, and survival prediction loss, to effectively guide the expression of differential information while maintaining synergy between modalities. Furthermore, we propose the Deep Holistic Orthogonal Fusion strategy (DHOF), which is used to integrate shared and unique features to achieve collaborative modeling and deep fusion of complex relationships between and within modalities. Extensive experiments on six TCGA cancer cohorts demonstrate that MurreNet significantly outperforms current mainstream methods in survival analysis tasks, demonstrating excellent prediction accuracy and robustness, fully demonstrating its potential clinical application value in the field of precision medicine.

The following is the citation information of the paper:

Mingxin Liu, Chengfei Cai, Jun Li, Pengbo Xu, Jinze Li, Jiquan Ma, and Jun Xu, MurreNet: Modeling Holistic Multimodal Interactions Between Histopathology and Genomic Profiles for Survival Prediction, MICCAI 2025 , September 23-27, 2025.

---

*This page was translated from the [original Chinese source](https://imic.nuist.edu.cn/info/1032/1423.htm).*
