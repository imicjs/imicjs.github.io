---
title: The research results of Cai Chengfei, a doctoral student in the Key Laboratory,
  were accepted by Bioinformatics, a top journal in bioinformatics.
date: '2025-05-12T00:00:00+08:00'
summary: 'Cai Chengfei, a doctoral student in the Key Laboratory (mentor: Professor
  Xu Jun), has made progress in the field of medical artificial intelligence. His
  research paper on "Prediction of Crohn''s Disease Treatment Response Based on the
  Fusion of Clustering and Weakly Supervised Learning" was officially accepted by
  the…'
type: blog
categories:
- Comprehensive news
tags:
- IMIC
- News·Notifications
source_url: https://imic.nuist.edu.cn/info/1032/1393.htm
source_language: zh-CN
translation_status: machine-translated-and-terminology-normalized
---

Cai Chengfei, a doctoral student in the Key Laboratory (mentor: Professor Xu Jun), has made progress in the field of medical artificial intelligence. His research paper on "Prediction of Crohn's Disease Treatment Response Based on the Fusion of Clustering and Weakly Supervised Learning" was officially accepted by the top bioinformatics journal "Bioinformatics". This achievement is an important manifestation of the cross-medical collaboration between the Key Laboratory and the Pathology Department of Drum Tower Hospital Affiliated to Nanjing University School of Medicine (directed by the team of Director Liu Yao and Director Sun Qi), and provides an innovative AI solution for the precise treatment of Crohn's disease.

Research background

Crohn's disease is a chronic inflammatory gastrointestinal disease that can affect any part of the digestive tract from the mouth to the anus, and often involves the terminal ileum and colon. It affects individuals of almost all ages, with more than 80% of patients diagnosed before the age of 40. Clinically, Crohn's disease may lead to intestinal strictures, fistulas, and abscess formation. Within 10 years of diagnosis, approximately 71% of patients require surgery to remove intestinal lesions. The symptom recurrence rate of patients within 10 years after surgery is approximately 40%, and endoscopic examination results within 3 years after surgery show a recurrence rate of 85%. Treatment of Crohn's disease primarily consists of nutritional support and medications, including corticosteroids, immunosuppressives, and biologics. Anti-TNF drugs, such as infliximab and adalimumab, are effective in inducing remission. However, after a period of treatment, some patients experience recurrence of the disease and need to switch to other drugs. Therefore, early identification of treatment response to specific drugs in Crohn's disease patients is critical for disease monitoring and development of optimal treatment strategies.

Ustekinumab (UST) is a novel monoclonal antibody that treats Crohn's disease by inhibiting interleukin 12/23 (IL-12/23) signaling, thereby reducing inflammation. It has been shown to be effective in improving clinical symptoms and delaying surgery. However, predicting individual response to this drug treatment remains difficult due to the lack of reliable histopathological biomarkers and the complexity of tissue morphology. Although recent deep learning methods have been widely used for quantitative analysis of panoramic slices, most methods lack effective mechanisms to select regions relevant to drug treatment response and integrate image patch-level features into robust patient-level predictions. Therefore, a framework capable of capturing local histological cues and global tissue context is urgently needed to improve predictive model performance.

research methods

This paper proposes a new clustering-enhanced weakly supervised learning framework, which is based on the fusion paradigm of clustering and weakly supervised learning to construct a model for predicting the therapeutic response of Crohn's disease patients to uskinumab. The model is based on panoramic endoscopic biopsy sections of Crohn's disease patients before treatment. In the study, continuous histological sample sections were used for analysis to achieve the task of automatically predicting whether Crohn's disease patients will respond to uskinumab treatment. The model avoids the burden of local area annotation by utilizing feature domain clustering and multi-instance feature fusion mode, and using the patient's panoramic slice level response to uskinumab treatment efficacy as the training label for the weakly supervised learning model.

![The research results of Cai Chengfei, a doctoral student in the Key Laboratory, were accepted by Bioinformatics, a top journal in bioinformatics.](https://imic.nuist.edu.cn/__local/0/BD/73/F825A018BA4050C6BC38B2D9E3D_B271D3D9_B2201.png)

Figure 1: is an overview of the research framework of this article. The prediction model framework studied in this article consists of five main parts: (1) preprocessing and standardization of panoramic slices; (2) building an image patch screening model to identify effective image patches for uskinumab treatment response prediction; (3) using selected image patches to develop patch-level uskinumab treatment response prediction models; (4) fusing the predicted image patch results and generating feature representations for each panoramic slice; (5) establishing a panoramic slice-level uskinumab treatment response prediction model.

First, this paper uses a pre-trained vision base model to encode image patches in panoramic images, and then applies a K-means clustering model to identify representative tissue morphology patterns. Discriminative image patches related to uskinumab treatment outcomes were filtered through a DenseNet-based classifier, and the predictions were interpreted using the Grad-CAM model. To aggregate the prediction results at the patch level, this paper adopts a multi-instance learning method to construct panoramic image features using patch likelihood histograms and bag-of-words representations. Finally, these features are used to train a classifier for final prediction of efficacy. The experimental results of the model proposed in this article on an independent test set show that our panoramic slice-level model achieves excellent prediction performance, with an AUC of 0.938 (95% CI: 0.879-0.996), a sensitivity of 0.951, and a specificity of 0.825, which is better than the currently published baseline image block-level model. Experimental results show that this model shows excellent prediction performance on the test set and can accurately evaluate the treatment response of Crohn's disease patients to uskinumab. These findings confirm the reliability of this approach in predicting biologic treatment response, with the model demonstrating good interpretability and generalization capabilities. This prediction model has clinical application value and is expected to provide reliable decision support for doctors to formulate individualized treatment plans.

experimental design

The experimental data used in this study included 402 H&E stained histopathological panoramic images. All image samples were derived from endoscopic biopsy tissue sections of clinically confirmed Crohn's disease patients. Inclusion criteria for study subjects: 1) All patients were diagnosed with Crohn's disease; 2) Have received treatment with uskinumab; 3) Baseline endoscopy showed disease activity and the SES-Crohn's disease score was significantly higher than 3 points; 4) The follow-up time was at least more than 24 weeks, and endoscopic re-examination was completed; refer to the "Chinese Consensus on the Diagnosis and Treatment of Inflammatory Bowel Disease (2018 Beijing)", and comprehensively diagnose Crohn's disease based on the patient's clinical manifestations, endoscopy, imaging, pathological examination, etc. Exclusion criteria: 1) age less than 18 years old; 2) failure to complete endoscopic review; 3) incomplete baseline data; 4) switching to other drugs due to non-efficacy related factors. All biopsies from Crohn's disease patients were treated with uskinumab, with 236 samples showing a response to uskinumab and 166 samples showing no response.

Experimental results

In the construction of the integrated model based on image patch clustering, this article randomly selected 50 panoramic slice samples, of which 29 samples had panoramic slices that responded to uskinumab treatment, and 21 samples did not have panoramic slices that responded to uskinumab treatment. A total of 329,045 image patches were generated from all samples as the data set for the mean clustering algorithm used in this article. The Calinski-Harabasz index is used to evaluate the optimal number of clusters. The Calinski-Harabasz index is calculated as the ratio of between-cluster variance to within-cluster variance. The higher the Calinski-Harabasz index value, the better the clustering performance, indicating that the clusters are well separated and unique. The clustering results and evaluation are shown in Figure 2.

![The research results of Cai Chengfei, a doctoral student in the Key Laboratory, were accepted by Bioinformatics, a top journal in bioinformatics.](https://imic.nuist.edu.cn/__local/1/84/42/2E2E670FF1DA229B85BB233F1B5_F0873CFB_272C07.png)

Figure 2: Results of image patch clustering and selection

After constructing a clustering approach to identify and filter image patches in panoramic slices that are highly correlated with treatment response. This paper builds a block-level treatment response prediction model based on selected image blocks to train, and then uses the extracted pathological features to train a classifier to build a panoramic slice-level treatment response prediction model, so that it can judge the treatment response of uskinumab in patients with Crohn's disease on unlabeled panoramic slice data. The prediction performance of its image block level and panoramic slice level models is shown in Figure 3:

![The research results of Cai Chengfei, a doctoral student in the Key Laboratory, were accepted by Bioinformatics, a top journal in bioinformatics.](https://imic.nuist.edu.cn/__local/C/A5/B7/FB88E78CCD07B0CA9D5A628A391_897C84CC_684D2.png)

Figure 3: Evaluation of image patch-level models and panoramic slice-level models. (a) Predicting patch-level Uskinumab responses using the DenseNet121 model. (b) Visualization of the distribution of uskinumab responsive and non-responsive cases in two-dimensional space using t-SNE. (c) AUC values ​​of the prediction results of all classifiers at the panoramic slice level. (d) Confusion matrix of test results of the model in the test set.

Conclusion

This study proposes a prediction model based on the fusion of clustering and weakly supervised learning, which can autonomously learn key morphological features of uskinumab treatment response from histopathological panoramic sections of Crohn's disease patients. This model has the following innovative advantages: first, it uses a clustering algorithm to automatically identify similar samples and select image areas that contribute most to classification, completely avoiding the need for manual annotation; second, it achieves global diagnosis prediction by selectively fusing discriminative features of key image areas and combining it with a multi-instance learning strategy.

The prediction model, based on pre-treatment biopsy panoramic slide data, demonstrated excellent predictive performance for uskinumab efficacy in the test cohort. Next, we plan to apply this model to prospective clinical studies to provide decision support for the development of individualized treatment plans for patients with Crohn's disease. In addition, this framework has good scalability and can be migrated to treatment response prediction tasks for other similar diseases in the future, assisting clinicians in optimizing treatment strategies, and ultimately improving patient clinical outcomes.

Chengfei Cai, Ruidong Chen, Jieyu Chen, Jun Li, Caiyun Lv, Yiping Jiao, Lanqing Wu, Juan Chen, Qi Sun, Qianyun Shi, Jun Xu,Wen Tang, Yao Liu, Predicting Ustekinumab Treatment Response in Crohn’s Disease Using Pre-Treatment Biopsy Images, Bioinformatics , 2025.

---

*This page was translated from the [original Chinese source](https://imic.nuist.edu.cn/info/1032/1393.htm).*
