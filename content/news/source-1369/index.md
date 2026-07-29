---
title: The paper collaborated by the key laboratory and the team of Professor Wu Xiaohua
  from the Department of Gynecology and Oncology of Fudan University Cancer Hospital
  was accepted by the journal Bioinformatics
date: '2025-01-26T00:00:00+08:00'
summary: Recently, teacher Wang Xiangxue and graduate student Cui Haoyu of the Key
  Laboratory of Pathology Wisdom Diagnosis and Treatment Team studied the prediction
  method of molecular subtypes of endometrial cancer based on conventional hematoxylin
  and eosin (H&E) stained Whole Slide Images (WSI) pathological sections. The…
type: blog
categories:
- Comprehensive news
tags:
- IMIC
- News·Notifications
source_url: https://imic.nuist.edu.cn/info/1032/1369.htm
source_language: zh-CN
translation_status: machine-translated-and-terminology-normalized
---

Recently, teacher Wang Xiangxue and graduate student Cui Haoyu of the Key Laboratory of Pathology Wisdom Diagnosis and Treatment Team studied the prediction method of molecular subtypes of endometrial cancer based on conventional hematoxylin and eosin (H&E) stained Whole Slide Images (WSI) pathological sections. The research results (Prediction of molecular subtypes for endometrial cancer based on hierarchical foundation model) were recently accepted by the journal Bioinformatics. Based on the currently excellent computational pathology large model UNI, this paper proposes a hierarchical classification model based on weakly supervised learning, hierarchical UNI (hi-UNI). Our proposed model was subjected to 5-fold cross-validation in the oncology and gynecology cohort of Fudan University Cancer Hospital (N=364), and its prediction accuracy for molecular subtypes of endometrial cancer reached a macro-average AUROC of 0.879 (95% CI, 0.853-0.904). Compared with the current state-of-the-art endometrial cancer molecular subtype prediction methods, the model proposed in this article is superior in both prediction accuracy and computational efficiency; in addition, our method has better reproducibility. This study aims to solve the time and cost of traditional gene sequencing typing: our method provides a reliable and convenient alternative to gene sequencing and is expected to change the field of endometrial cancer diagnosis. The intelligent pathology auxiliary diagnosis and treatment team of the Key Laboratory of Intelligent Medical Image Computing has long been committed to ultra-high-resolution pathological image processing and analysis. The clinical cooperation unit of this paper is Professor Guo Qinhao and Professor Wen Hao from the team of Professor Wu Xiaohua, Department of Gynecology Oncology, Fudan University Cancer Hospital.

Research background

Endometrial carcinoma is one of the most common gynecological malignant tumors today. In recent years, four molecular classifications consisting of POLE mut, mismatch repair deficient (MMRd), p53 abnormality, and no special molecular alteration (NSMP) have gradually replaced traditional classification methods and become the mainstream classification method in recent years. They play an important role in guiding diagnosis, treatment and prognosis. These four classifications rely on gene sequencing, which is relatively expensive and has a long cycle. At present, diagnosis based on pathological slices is still an indispensable and important method in the diagnosis and treatment cycle of endometrial cancer. With the development of digital pathology technology, especially the application of digital slide scanners, it provides a technical foundation for the close integration between pathology and molecular biology. This approach brings the possibility of observing morphological changes from genetic mutations to indirectly predicting mutation information of specific genes. This study attempts to extract key information from hematoxylin and eosin-stained whole-section images to quickly and accurately predict four molecular types of endometrial cancer.

Classification based on WSI can be divided into methods based on MIL (multi-instance learning) and classical weakly-supervised methods (Narmin et al.). The endometrial cancer molecular classification prediction network im4MEC proposed by Fremond et al. is a MIL method. The performance of its necessary feature extractor relies on a large amount of data and high computing power, which is a huge challenge for most institutions to reproduce. This study proposes an end-to-end endometrial cancer molecular classification prediction model hi-UNI, which is based on the traditional weak supervision method and is improved based on the characteristics of the pyramid structure of digital pathology images, so that it can combine the macroscopic characteristics of tissues and the microscopic characteristics of cells at different resolutions. Its innovation lies in:

1. Use the prior knowledge of large models and powerful feature extraction capabilities, and use weak supervision methods to fine-tune, solving the problem of large-scale data dependence and computing power dependence.

2. Use a hierarchical structure to integrate WSI information at different scales, solving the problem that large models based on ViT can only accept a fixed resolution (224 pixels).

experiment

This study collected 378 hematoxylin and eosin (H&E) stained WSIs from 333 endometrial cancer patients admitted to the Department of Gynecology Oncology, Fudan University Cancer Hospital from 2020 to 2023. This dataset integrates comprehensive clinical annotation, patient clinical data, and 46-gene NGS data.

Figure 1 Experimental process and network structure diagram of this article

We use histograms to distinguish foreground and background areas, and use a tumor segmentation network based on DeepLab v3 to crop and retain image patches in the tumor area, and use selective sampling to divide image patches from the same area into three patches of different scales, which are sent to the parallel UNI for fine-tuning, feature fusion and prediction output respectively. The final WSI-level prediction result is derived from the soft voting of all image patches. Specifically, the WSI-level prediction probability of molecular subtype j can be obtained by the following formula:

![The paper collaborated by the key laboratory and the team of Professor Wu Xiaohua from the Department of Gynecology and Oncology of Fudan University Cancer Hospital was accepted by the journal Bioinformatics](https://imic.nuist.edu.cn/__local/5/D6/C4/7FAEB66EADC62EEAD3397C3C36E_25BC29D8_1560.png)

Among them, N represents the total number of extracted hierarchical image patches, z i represents the logits output of the network corresponding to image patch i. Softmax ( z i ) j is the Softmax function output probability for subtype j calculated from the logarithm z i . We compare the proposed weakly supervised hi-UNI with current top-performing MIL methods, including recent methods such as TransMIL, DTFD-MIL, and SETMIL, as well as classic MIL methods such as CLAM-SB and Attention-MIL (implemented in im4MEC). In terms of WSI prediction, our proposed method achieved an AUROC of 0.829 (95% CI, 0.816-0.843) on MMRd typing, an AUROC of 0.899 (95% CI, 0.867-0.931) on NSMP, and an AUROC of 0.899 (95% CI) on p53abn. , 0.836-0.962) AUROC, POLE mut reached an AUROC of 0.886 (95% CI, 0.853-0.919), and its ROC curve is as shown in the figure:

Figure 2 ROC curve of the proposed method.

In the five-fold cross-validation experiment, TransMIL using UNI as the feature extractor performed better than other MIL methods, with an AUROC of 0.838 (95% CI: 0.805-0.871). Our proposed method outperformed TransMIL on MMRd, NSMP and POLE mutation subtypes, achieving a macro-average AUROC of 0.879 (95% CI: 0.853-0.904), with slightly lower performance on p53abn classification. The specific results are shown in the figure:

Figure 3 Comparison of experimental results and tSNE characteristic distribution

The distribution of four typing features obtained using tSNE is shown in the right subfigure. The UNI model on the left subfigure can distinguish the typing subtypes of image patches based on the key features it extracts, including NSMP (green scatter) and p53abn (red scatter), but has difficulty when dealing with highly similar image patches - the clusters of each subtype have not been clearly distinguished - this also applies to hi-UNI without fine-tuning. The right figure shows that both the UNI and hi-UNI models can significantly improve the feature extraction effect after fine-tuning on the endometrial cancer data set, and the clustering of feature vectors corresponding to different subtypes is more obvious, which shows that weakly supervised learning can improve the feature representation of classification. Compared with UNI (Figure c), the clustering of hi-UNI (Figure d) is more aggregated, the cluster edges between different subtypes are more obvious, and the clustering edges between different subtypes are more obvious, showing more prominent subtype-related characteristics.

Conclusion

In this study, we investigated hierarchical networks based on weakly supervised learning pipelines and computational pathology-based models for endometrial cancer molecular subtype prediction. Our approach achieves state-of-the-art performance in the field, providing cost-effective and fast molecular subtype prediction, while proposing a new method of fine-tuning the underlying model to improve feature extraction in computational pathology. This innovation not only improves the utility of the underlying model in pathology but also opens new avenues for predicting disease subtypes using WSI.

The following is the citation information of the paper:

Haoyu Cui, Qinhao Guo, Jun Xu, Xiaohua Wu, Chengfei Cai, Yiping Jiao, Wenlong Ming, Hao Wen, Xiangxue Wang, Prediction of molecular subtypes for endometrial cancer based on hierarchical foundation model, Bioinformatics , 2025;, btaf059, https://doi.org/10.1093/bioinformatics/btaf059

---

*This page was translated from the [original Chinese source](https://imic.nuist.edu.cn/info/1032/1369.htm).*
