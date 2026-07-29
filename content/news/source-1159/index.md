---
title: The paper jointly written by Zhou Zhenghao, a graduate student at the Smart
  Medical Research Institute, and Dr. Xia Yi from CUHK Hospital was accepted by Radiology,
  the top journal in the field of medical imaging.
date: '2023-04-27T00:00:00+08:00'
summary: Research
type: blog
categories:
- Comprehensive news
tags:
- IMIC
- News·Notifications
source_url: https://imic.nuist.edu.cn/info/1032/1159.htm
source_language: zh-CN
translation_status: machine-translated-and-terminology-normalized
---

Research background

With the innovation of imaging diagnosis technology, advances in surgical procedures, and the use of targeted and immunological drugs, the overall survival of patients with hepatocellular carcinoma (HCC) has greatly improved, but the 5-year survival is still low. One of the reasons is that patients already have microvascular invasion (MVI) when they are diagnosed. MVI refers to the invasion of microvessels by tumors. Under the microscope, nests of cancer cells are seen in the vascular lumen lined with endothelial cells. They are commonly found in small portal vein branches and hepatic vein branches in the adjacent liver tissue, as shown in Figure 1. The incidence rate of MVI is between 15% and 57.1%. Its occurrence indicates that the biological behavior of HCC is more aggressive. Therefore, it is an important factor affecting the prognosis of liver cancer and an important reference for the formulation of treatment plans. In recent years, a large number of studies have attempted to use CT, MRI and other imaging methods combined with clinical and laboratory indicators to predict MVI preoperatively, which can help guide treatment decisions for patients with liver cancer.

![The paper jointly written by Zhou Zhenghao, a graduate student at the Smart Medical Research Institute, and Dr. Xia Yi from CUHK Hospital was accepted by Radiology, the top journal in the field of medical imaging.](https://imic.nuist.edu.cn/__local/4/C7/32/DCD1C060ACEC16569D5368CD464_CB7982A8_6D316.png)

Figure 1 Manifestations of microvascular invasion process in hepatocellular carcinoma

Since its establishment in 2021, the Nanjing University of Information Science & Technology-Zhongda Hospital Smart Medical Research Institute has been committed to research on cancer lesion area segmentation, disease type prediction, and survival prognosis through medical data such as medical images and pathological slices. Recently, the team proposed a novel method to predict MVI by building a radiomics model based on four-phase CT images after preoperative registration, and revealed the potential biological mechanism of MVI. In addition, this method can also be flexibly applied to the study of other registered multi-modal data. The research results (Predicting Microvascular Invasion in Hepatocellular Carcinoma using CT-based Radiomics Model) have been published online in Radiology (IF = 29.15).

1. Introduction

Previous studies have shown that various clinical and radiological characteristics—such as serum alpha-fetoprotein, tumor size, and two-trait predictor of venous invasion (TTPVI)—are independent predictors of MVI. Imaging examinations, especially CT examinations, are crucial for the routine diagnosis and evaluation of HCC. Radiomics is an emerging form of imaging analysis that can be used to obtain useful information in a high-throughput manner, which has the potential to transform digital medical images into countless quantitative features that reveal pathophysiology. Recently, it has been reported that a radiomics model can accurately predict MVI based on CT images. Until now, preoperative prediction of MVI has been challenging because MVI is a histopathological finding that can only be diagnosed from postoperative surgical specimens.

To alleviate the above challenges, this study first established and tested a model to predict microvascular invasion (MVI) based on multi-phase CT radiomics features in patients with hepatocellular carcinoma. Then, a preliminary study was conducted to finally identify MVI-related differentially expressed genes. The main contributions of this study are summarized as follows:

• Developed a new radiomics method, constructed Delta radiomics features through image registration and subtraction methods, successfully quantified the changes in CT image enhancement and added them to the model. It was found that the performance of the model was improved, and the model was able to stratify patient prognosis.

• At the transcriptome level, it was found that in the MVI-positive group, MVI-related differentially expressed genes (derived from image features) were involved in more glucose metabolism, while immune cell infiltration within the tumor was reduced.

2. Method

Figure 2 shows the radiomics research process of this study, which can be roughly summarized into the following five points:

l Liver area registration is performed using deep learning algorithms and Elastix (using the portal venous phase as a fixed image).

l Manually outline the 3D tumor region of interest (VOI) in the registration map, and extend it 5 mm outward through the algorithm as the peritumoral area (erasing non-liver parenchymal tissue); generate a subtraction image through the registration image.

l Extract radiomics features, make a difference between the radiomics features of different phases, and generate Delta1 radiomics features; extract features from subtraction images and define them as Delta2 radiomics features.

l The modeling strategy adopted is to use ICC to evaluate feature stability, mRMR and LASSO to reduce feature dimensionality, and finally mainly use logistic regression to build the model.

l Establish and test radiomics models and hybrid models in cohorts 1-3, verify the prognostic stratification ability of the model in cohort 4, and explore the potential biological mechanisms of MVI in cohort 5.

![The paper jointly written by Zhou Zhenghao, a graduate student at the Smart Medical Research Institute, and Dr. Xia Yi from CUHK Hospital was accepted by Radiology, the top journal in the field of medical imaging.](https://imic.nuist.edu.cn/__local/F/13/AA/2A911A561648855CB7357986404_713CF931_CBF64.jpg)

Figure 2 Radiomics flow chart

3. Experiments and results

This study retrospectively included the preoperative imaging and clinical data of 773 patients with HCC diagnosed by surgical pathology from four medical centers and the TCIA database. Center 1 was divided into a training cohort (n=334) and an internal testing cohort (n=142) on a 7:3 basis, centers 2-3 were combined into an external testing cohort (n=141), center 4 was a prognostic cohort (n=121), and center 5 was a TCIA cohort (n=35). MVI was confirmed by surgical pathology, centers 1-3 had MVI tags, centers 4-5 did not have MVI tags, center 4 had early recurrence-free survival and overall survival data, and center 5 had RNA sequencing data. Table 1 describes the sample distribution of the dataset and its image features.

Characteristics

Training set

( n = 334)

Internal test set

( n = 142)

External test set

(n = 141)

Outcome cohort

( n = 121)

TCIA set

( n = 35)

Patient demographics

Age (years) *

59 (51-66)

57 (49-64)

55 (49-63)

53 (46-59)

65 (56-70)

Sex (male)

287 (85.9%)

120 (84.5%)

111 (78.7%)

95 (78.5%)

20 (64.5%)

HBV infection

254 (76.0%)

109 (76.8%)

115 (81.6%)

90 (74.4%)

18 (51.4%)

BCLC stage (0 or A)

324 (97.0%)

139 (97.9%)

136 (96.5%)

118 (97.5%)

31 (88.6%)

Liver cirrhosis

215 (64.4%)

87 (61.3%)

112 (79.4%)

67 (55.4%)

N/A

Clinical parameters

Child-Pugh grade (A)

322 (96.4%)

136 (95.8%)

138 (97.9%)

111 (91.7%)

22 (71.0%)

AFP (ng/mL) *

22.1 (4.5-236.7)

13.4 (3.6-217.5)

41.1 (4.7-448.9)

25.4 (5.0-246.0)

10.0 (3.0-116.5)

ALT (U/L) *

28 (23-38)

26 (17-35)

33 (24-44)

34 (24-50)

N/A

AST (U/L) *

28 (23-38)

26 (22-33)

34 (24-48)

35 (25-52)

N/A

Radiological features

Max tumor diameter (cm) *

3.5 (2.2-5.0)

3.4 (2.2-5.0)

3.5 (2.2-6.0)

5.3 (3.8-8.0)

6.9 (3.9-11.3)

Tumor number (solitary)

316 (94.6%)

134 (94.4%)

136 (96.5%)

118 (97.5%)

31 (88.6%)

Pseudocapsule (ill-defined)

123 (36.8%)

50 (35.2%)

39 (27.7%)

44 (36.4%)

10 (28.6%)

TTPVI (present)

81 (24.3%)

34 (23.9%)

37 (26.2%)

39 (32.2%)

9 (25.7%)

Peritumoral enhancement (present)

55 (16.5%)

20 (14.1%)

22 (15.6%)

31 (25.6%)

7 (20.0%)

Margin (non-smooth)

148 (44.3%)

46 (32.4%)

67 (47.5%)

62 (51.2%)

17 (48.6%)

MVI (present)

120 (35.9%)

44 (31.0%)

54 (38.3%)

N/A

N/A

Table 1Basic characteristics of patients

Table 2 shows the logistic regression analysis of relevant variables in MVI patients in the training set. It can be seen that pseudocapsule, TTPVI, peritumoral enhancement and radiomics scores are independent risk factors for predicting MVI (p<0.01).

Characteristics

Univariable analysis

Multivariable analysis

OR (95% CI)

P value

OR (95% CI)

P value

Age, ≤50 vs >50 years

0.63 (0.38, 1.05)

.08

Sex, male vs female

1.23 (0.64, 2.38)

.54

HBV infection, absent vs present

1.06 (0.62, 1.78)

.84

BCLC stage, 0 or A vs B

1.82 (0.52, 6.41)

.35

Liver cirrhosis, absent vs present

0.99 (0.62, 1.57)

.95

Child-Pugh grade, a vs b

2.59 (0.80, 8.35)

.099

AFP, ≤ 200 vs > 200 ng/mL

2.19 (1.34, 3.59)

.002

ALT, ≤ 50 vs > 50 U/L

1.30 (0.72, 2.34)

.38

AST, ≤ 40 vs > 40 U/L

1.62 (0.96, 2.73)

.07

Max tumor diameter, ≤ 5 vs > 5 cm

3.18 (1.86, 5.46)

< .001

Tumor number, solitary vs multiple

1.46 (0.56, 3.80)

.44

Pseudocapsule, well-defined vs ill-defined

2.40 (1.51, 3.81)

< .001

4.50 (2.45-8.28)

< .001

TTPVI, absent vs present

8.44 (4.78, 14.90)

< .001

6.78 (3.39-13.54)

< .001

Peritumoral enhancement, absent vs present

5.96 (3.15, 11.26)

< .001

3.20 (1.50-6.84)

< .001

Margin, smooth vs non-smooth

0.80 (0.51, 1.26)

.34

Radiomics score (continuous)

2.73 (2.09, 3.56)

< .001

2.23 (1.65-3.02)

< .001

Table 2 Clinical and imaging features in the training set

Table 3 shows the performance of the Radiomics model built using all radiomics features and the Hybrid model built by adding clinical and imaging features on the training set, internal test set and external test set. It can be seen that by integrating the four aforementioned imaging features, the performance of the hybrid model has been further improved.

Model and Metric

Radiomics model

Hybrid model #

P value

Training set ( n = 334)

Sensitivity

71 (85/120)

83 (100/120)

.001

Specificity

71 (153/214)

78 (167/214)

.08

Accuracy

71 (238/334)

80 (267/334)

.001

AUC*

0.76 (0.71, 0.82)

0.85 (0.81, 0.89)

< .001

Internal test set ( n = 142)

Sensitivity

80 (35/44)

80 (35/44)

> .99

Specificity

66 (65/98)

80 (78/98)

< .001

Accuracy

70 (100/142)

80 (113/142)

.007

AUC*

0.76 (0.68, 0.84)

0.86 (0.79, 0.93)

.002

External test set ( n = 141)

Sensitivity

65 (35/54)

74 (40/54)

.27

Specificity

74 (64/87)

85 (74/87)

.04

Accuracy

70 (99/141)

81 (114/141)

.01

AUC*

0.72 (0.63, 0.81)

0.84 (0.78, 0.91)

< .001

Table 3 Diagnostic performance of hybrid and radiomics models

In the prognostic cohort, the patient MVI prediction scores obtained by the radiomics model (optimal) and the mixed model can both risk stratify the early recurrence survival (recurrence within 2 years) and overall survival of liver cancer patients, as shown in Figure 3. Among them, (A, B) 1-year and 2-year recurrence-free survival and (C, D) 1-year, 3-year and 5-year overall survival were evaluated using radiomics model-derived scores and mixed model-derived scores. Low model scores are represented by red lines, high model scores are represented by yellow lines.

Figure 3 Survival curve

Figure 4 shows that in the TCIA cohort, based on MVI-related imaging features, we screened out related MVI differential genes. Enrichment analysis of these MVI-related differential genes revealed that sugar metabolism and other related pathways were enriched in the MVI high-risk group, especially the glycolysis and pentose phosphorylation pathways. In addition, the expression levels of immune cells in each group were explored according to the imaging characteristics related to MVI, and the correlation between immune infiltration and MVI was explored. It was found that among various immune cells, the level of immune infiltration in the MVI high-risk group was lower than that in the MVI low-risk group, especially CD8+ T cells.

Figure 4 Screening of related genes

It can be seen from Figure 5 that the hybrid model successfully predicted the MVI status of the two patients. (a-b) 57-year-old male patient with negative MVI. CT shows a 9.5-cm tumor without TTPVI (black and white arrow), peritumoral enhancement, and clear pseudocapsule (red arrow). Immunohistochemistry showed abundant CD8+ T cell infiltration in the tumor. The patient has no recurrence after surgery and has been alive for 82.3 months. (c-d) 35-year-old male patient with positive MVI and CT scan showing a 10.9-cm tumor. The tumor shows peritumoral enhancement (yellow arrow), TTPVI, and an ill-defined pseudocapsule. Immunohistochemistry showed that CD8+ T cells were sparse within the tumor. The patient relapsed 3.4 months after surgery and died 13.5 months later.

Figure 5 CT images and CD8+ T cell immunohistochemistry of two HCC patients

Summary

In order to alleviate the difficulties and challenges in predicting the MVI status of HCC patients, this study constructed a Hybrid model that combined CT radiology and radiomics features to successfully predict the microvascular invasion (MVI) status of hepatocellular carcinoma patients. We also found that MVI-related differentially expressed genes are usually involved in glucose metabolism. Further studies are needed to ensure the generalizability of our model and to test the biological relevance of our transcriptome sequencing results in cell or animal experiments.

With the development of advanced medical image analysis tools, we can more easily extract multi-scale image biomarkers of disease, such as millimeter- and micron-scale image phenotypes, from imaging and histopathology sections. These multiscale image biomarkers can help doctors more accurately detect and diagnose disease from imaging and histology images, and try to predict recurrence risk, disease aggressiveness, patient survival, and patient response to treatment. The Smart Medical Research Institute has long been committed to exploring advanced machine learning-driven imaging and histological image analysis methods, through the extraction and analysis of "image biomarkers" from imaging images and digital tissue samples, to assist doctors in improving disease prevention, diagnosis and prognosis and better evaluating patients' response to treatment.

The research team of the Smart Medical Research Institute is a team of experts and students from different disciplines such as medicine and engineering. They use their professional knowledge to jointly solve problems in the medical field. The advantage of the medical-engineering interdisciplinary team is that it can integrate multiple resources and perspectives, innovate medical technologies and methods, improve medical quality and efficiency, and promote the development of the medical industry. This paper is the result of a long-term collaboration between the engineering team led by Professor Xu Jun from Nanjing University of Information Science & Technology and the medical team led by Professor Ju Shenghong from Zhongda Hospital. They work together to combine medicine, engineering technology and other disciplines to solve major problems in the field of life and health. The institute promotes basic and applied research in medicine and life sciences through interdisciplinary research between medicine and engineering, thereby improving the level and efficiency of doctors’ diagnosis and treatment of diseases and contributing to human health and well-being. At the same time, interdisciplinary research between medicine and engineering can also stimulate cooperation and exchanges between science and engineering scientists and medical scientists, expand their knowledge horizons and ways of thinking, cultivate talents with interdisciplinary abilities and innovative spirit, and provide impetus for scientific and technological progress and social development.

---

*This page was translated from the [original Chinese source](https://imic.nuist.edu.cn/info/1032/1159.htm).*
