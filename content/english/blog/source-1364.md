---
title: The papers of key laboratory teacher Luo Yuemei and graduate student Li Yuan were accepted by the journal Knowledge-Based Systems
meta_title: The papers of key laboratory teacher Luo Yuemei and graduate student Li Yuan were accepted by the journal Knowledge-Based Systems
description: Teacher Luo Yuemei and her team from the Key Laboratory of Intelligent Medical Image Computing have been committed to the research of OCT imaging and analysis and deep learning automatic recognition algorithms. Recently, Teacher Luo and his team proposed a new semi-supervised learning (SSL) method that combines…
date: '2024-12-27T00:00:00+08:00'
image: /images/content/source-1364.jpg
categories:
- News
- Comprehensive news
author: IMIC Lab
tags:
- IMIC
- News
draft: false
source_url: https://imic.nuist.edu.cn/info/1032/1364.htm
translation_status: machine-translated-and-terminology-normalized
---

Teacher Luo Yuemei and her team from the Key Laboratory of Intelligent Medical Image Computing have been committed to the research of OCT imaging and analysis and deep learning automatic recognition algorithms. Recently, Teacher Luo and his team proposed a new semi-supervised learning (SSL) method that combines category-aware contrast learning with FixMatch to enhance the robustness and accuracy of retinal disease identification using minimal labeled data. This research result (Retinopathy Identification in Optical Coherence Tomography Images Based on a Novel Class-Aware Contrastive Learning Approach (Retinopathy Identification in Optical Coherence Tomography Images Based on a Novel Class-Aware Contrastive Learning Approach)) was recently accepted by Knowledge-Based Systems (Journal of the First District of the Chinese Academy of Sciences, the latest impact factor of the magazine is 7.2). Teacher Luo Yuemei is the corresponding author of this article, and Li Yuan, a graduate student in the key laboratory, is the first author.

Research background

Computer vision technology plays an important role in retinal disease detection based on optical coherence tomography (OCT) images. However, this often relies on large labeled datasets that may be scarce. Detecting retinal diseases faces specific challenges, such as the need to accurately distinguish various subtle disease features and the need for large amounts of labeled data, which is often difficult and expensive to obtain. Furthermore, manual annotation of retinal images is labor-intensive and prone to human error. Semi-supervised learning, especially through pseudo-labeling, holds the promise of leveraging unlabeled data; however, it is not always resistant to confirmation bias.

1. Introduction

Previous research has the following shortcomings: first, the generation of pseudo-label accuracy greatly affects model quality; second, confirmation bias can damage the consistency constraints of unknown data, thus affecting the performance of the model; in addition, model training may require a large amount of labeled data.

To address the above shortcomings, this paper proposes a new semi-supervised learning (SSL) method that combines category-aware contrastive learning with FixMatch to enhance the robustness and accuracy of retinal disease identification using minimal labeled data, eliminating the need for additional annotations and domain knowledge.

To make robust predictions of confirmation bias in complex retinopathy OCT images, we construct a selected matrix from out-of-distribution data and reweight the predictions based on prediction scores, which can identify biases and prioritize clean data, thereby reducing overfitting to potentially incorrect pseudo-labels. This paper computes a supervised contrastive loss between features and weighting matrices to capture subtle class relationships. This helps build more discriminative models than those trained with traditional cross-entropy loss.

2. Method

Figure 1 is the algorithm flow chart of this paper, which can be divided into the following steps:

![The papers of key laboratory teacher Luo Yuemei and graduate student Li Yuan were accepted by the journal Knowledge-Based Systems](https://imic.nuist.edu.cn/__local/C/5E/98/870220E4D1FADF89C4704AF20FC_B4EE7976_72FF.jpg)

Figure 1 Algorithm flow chart

First, given a batch of labeled and unlabeled images, pass the labeled images to the prediction module to get .

![The papers of key laboratory teacher Luo Yuemei and graduate student Li Yuan were accepted by the journal Knowledge-Based Systems](https://imic.nuist.edu.cn/__local/8/D0/BB/59FB76843455033BBE4796DE847_4B248E22_17A.png)

Then, the prediction module receives weakly enhanced and strongly enhanced unlabeled images and computes .

![The papers of key laboratory teacher Luo Yuemei and graduate student Li Yuan were accepted by the journal Knowledge-Based Systems](https://imic.nuist.edu.cn/__local/8/48/F4/EB581DC28C1184A9FE711D41658_BA761A64_167.png)

Subsequently, the contrast module utilizes pseudo-labels generated from weakly enhanced images to construct a selection matrix through image-level contrast learning to reduce confirmation bias. By reweighting, clean data is prioritized to obtain a weighted matrix. Use two types of strongly enhanced images to construct a feature matrix and calculate .

![The papers of key laboratory teacher Luo Yuemei and graduate student Li Yuan were accepted by the journal Knowledge-Based Systems](https://imic.nuist.edu.cn/__local/E/34/6E/C748812C16D5C0BB5CAF3CC7207_0B29CC4E_17B.png)

Finally, the above three losses are weighted and combined, and the calculation formula is as follows: .

![The papers of key laboratory teacher Luo Yuemei and graduate student Li Yuan were accepted by the journal Knowledge-Based Systems](https://imic.nuist.edu.cn/__local/5/BF/55/E52150D931B720670C8D2DBF895_60761D2C_3E9.png)

Note: The model has two outputs: logistic values and eigenvalues. The solid line represents the eigenvalue or logical value, and the dotted line represents the logical value after obtaining the predicted score through softmax mapping.

3. Experimental results

To evaluate the algorithm, this paper uses three classic retinopathy datasets.

The first dataset, BOE, was proposed by Srinivasan et al. from Duke University. The BOE data set contains three image categories: AMD, DME and NORMAL, and a total of 45 subjects were collected. Among them, the images of the AMD, DME and NORMAL categories are 723, 1101 and 1407 respectively, totaling 3231 images.

The second dataset is RetinalOCT, originally introduced by Subramanian et al. The original data set included eight different retinopathy types. In this study, this paper focuses on three subsets: AMD, DME, and NORMAL. Each category contains 3000 images, for a total of 9000 OCT images.

The third dataset, CELL, was derived from a retrospective cohort of adult patients from July 1, 2013 to March 1, 2017 at the University of California, San Diego Healey Eye Institute, Retina Research Foundation, Medical Center Ophthalmology Associates, Shanghai First People's Hospital, and Beijing Tongren Eye Center. This dataset contains four image categories: CNV, DME, DRUSEN and NORMAL. There are 37,447, 11,590, 8,858 and 26,557 images in the CNV, DME, DRUSEN and NORMAL categories respectively, for a total of 84,452 images.

Figure 2 shows representative images of different lesions from the three datasets.

![The papers of key laboratory teacher Luo Yuemei and graduate student Li Yuan were accepted by the journal Knowledge-Based Systems](https://imic.nuist.edu.cn/__local/3/02/FD/70AAE21FE4E752475F26C5715FB_7B8DD557_1790A.png)

Figure 2 Examples of data set samples used in this paper

The experimental results are shown in Table 1-3. It is obvious that the SSL method greatly outperforms traditional supervised learning methods in terms of classification efficiency. Notably, our proprietary category-aware contrastive learning technique stands out as a superior method, outperforming all other metrics, achieving accuracy of 0.966, 0.964, and 0.957, sensitivity of 0.966, 0.964, and 0.957, and specificity of 0.983, 0.982, and 0.986 on BOE, RetinalOCT, and CELL datasets, respectively. Furthermore, the p-value results provide clear evidence that the proposed method outperforms existing methods.

Table 1 Experimental results on BOE data set

Method

Accuracy

STD

P-value

Sensitivity

Specificity

SVM+HOG

0.570

-

2.40E-18

0.570

0.785

CNN

0.802

0.067

7.30E-04

0.802

0.901

ResNet-18

0.601

0.046

1.28E-06

0.601

0.800

ResNet-18+Pretrain

0.840

0.022

1.12E-05

0.840

0.920

AlexNet

0.523

0.032

1.20E-09

0.523

0.761

AlexNet+Pretrain

0.754

0.017

1.97E-08

0.754

0.877

VGG-16

0.629

0.059

8.84E-07

0.629

0.814

VGG-16+Pretrain

0.855

0.025

3.64E-05

0.855

0.927

Pseudo-Labeling

0.903

0.021

1.13E-05

0.903

0.951

Temporal Ensembling

0.894

0.049

8.88E-04

0.894

0.947

Mean Teacher

0.926

0.038

4.04E-04

0.926

0.963

VGG+VAT

0.942

0.024

1.53E-02

0.942

0.971

DeFixmatch

0.937

0.007

3.34E-06

0.937

0.969

SoftMatch

0.951

0.012

4.12E-04

0.951

0.976

InfoMatch

0.922

0.004

1.84E-07

0.922

0.961

Proposed

0.966

0.002

-

0.966

0.983

Table 2 Experimental results on RetinalOCT data set

Method

Accuracy

STD

P-value

Sensitivity

Specificity

SVM+HOG

0.806

-

1.00E-12

0.806

0.903

CNN

0.789

0.009

3.28E-10

0.789

0.894

ResNet-18

0.821

0.027

9.49E-07

0.821

0.910

ResNet-18+Pretrain

0.870

0.022

5.71E-06

0.870

0.935

AlexNet

0.633

0.102

4.35E-05

0.633

0.817

AlexNet+Pretrain

0.835

0.053

3.67E-05

0.835

0.918

VGG-16

0.809

0.032

2.69E-06

0.809

0.904

VGG-16+Pretrain

0.908

0.017

5.18E-05

0.908

0.954

Pseudo-Labeling

0.899

0.013

5.62E-05

0.899

0.950

Temporal Ensembling

0.918

0.012

2.17E-04

0.918

0.959

Mean Teacher

0.931

0.008

2.72E-05

0.931

0.966

VGG+VAT

0.937

0.006

3.44E-05

0.937

0.969

DeFixmatch

0.953

0.016

1.64E-02

0.953

0.977

SoftMatch

0.950

0.007

4.75E-03

0.950

0.975

InfoMatch

0.930

0.005

2.86E-06

0.930

0.965

Proposed

0.964

0.004

-

0.964

0.982

Table 3 Experimental results on CELL data set

Method

Accuracy

STD

P-value

Sensitivity

Specificity

SVM+HOG

0.522

-

4.46E-19

0.522

0.841

CNN

0.556

0.036

2.61E-08

0.556

0.852

ResNet-18

0.569

0.033

1.35E-08

0.569

0.856

ResNet-18+Pretrain

0.826

0.033

1.82E-05

0.826

0.942

AlexNet

0.432

0.023

8.62E-11

0.432

0.811

AlexNet+Pretrain

0.837

0.027

2.45E-06

0.837

0.946

VGG-16

0.527

0.054

1.09E-07

0.527

0.842

VGG-16+Pretrain

0.844

0.022

3.64E-06

0.844

0.948

Pseudo-Labeling

0.916

0.017

1.42E-04

0.916

0.972

Temporal Ensembling

0.866

0.021

3.14E-05

0.866

0.955

Mean Teacher

0.883

0.041

1.45E-02

0.883

0.961

VGG+VAT

0.936

0.007

8.88E-05

0.936

0.979

DeFixmatch

0.936

0.006

3.33E-05

0.936

0.979

SoftMatch

0.943

0.004

1.37E-05

0.943

0.981

InfoMatch

0.866

0.003

2.61E-11

0.866

0.955

Proposed

0.957

0.002

-

0.957

0.986

Figure 3 shows the ROC and PR curves for all compared methods. It can be seen that the proposed method outperforms all other methods involved in the comparison, a finding consistent with the metrics shown in Tables 1-3.

![The papers of key laboratory teacher Luo Yuemei and graduate student Li Yuan were accepted by the journal Knowledge-Based Systems](https://imic.nuist.edu.cn/__local/B/E0/8B/44DB49BE929FA70A63C1EE1CBD9_CADDDA1A_8675.png)

![The papers of key laboratory teacher Luo Yuemei and graduate student Li Yuan were accepted by the journal Knowledge-Based Systems](https://imic.nuist.edu.cn/__local/1/17/D4/7FCC1CB809193A2406AF8891376_D5143007_7E0B.png)

![The papers of key laboratory teacher Luo Yuemei and graduate student Li Yuan were accepted by the journal Knowledge-Based Systems](https://imic.nuist.edu.cn/__local/7/20/DD/65FFDCF1C13758062FD48BC6077_16143968_7408.png)

![The papers of key laboratory teacher Luo Yuemei and graduate student Li Yuan were accepted by the journal Knowledge-Based Systems](https://imic.nuist.edu.cn/__local/7/A7/52/FE27A438F85D20214AF7BA61FD6_3618A00B_8BE1.png)

![The papers of key laboratory teacher Luo Yuemei and graduate student Li Yuan were accepted by the journal Knowledge-Based Systems](https://imic.nuist.edu.cn/__local/F/F1/93/45B366DD8A8A684D555B23EB165_65B52342_8F37.png)

![The papers of key laboratory teacher Luo Yuemei and graduate student Li Yuan were accepted by the journal Knowledge-Based Systems](https://imic.nuist.edu.cn/__local/6/6B/C4/7F886DE7E4C68B8E0AF394E097C_320575C3_80A4.png)

Figure 3 ROC and PR curves comparing experimental results

The confusion matrix of this paper’s method is shown in Figure 4. It is obvious that our method produces high classification accuracy for NORMAL and AMD classes. However, the identification accuracy of DME was slightly lower, which can be attributed to the scarcity of DME samples and the presence of samples with extremely small lesion areas. Despite this, the overall performance of this method is still very good.

![The papers of key laboratory teacher Luo Yuemei and graduate student Li Yuan were accepted by the journal Knowledge-Based Systems](https://imic.nuist.edu.cn/__local/3/B0/08/1410BC695E12541B3B030A2185B_5E2499B5_3CE1.jpg)

Figure 4 Confusion matrices of this paper’s algorithm on three data sets

In this paper, the CELL dataset contains 1000 OCT images annotated by 6 human ophthalmologists organized by Kermany et al. This paper compares the results of the proposed method with those of human experts, as shown in Figure 5. To evaluate the robustness of the proposed method, we use different numbers of labeled images (80 and 160) to train our model. Experimental results show that our model can provide performance comparable to human experts. In fact, with only 80 labeled images, our model performed better than two experts (the expert achieved the lowest accuracy of 92.1%). Our model has 160 labeled images, surpassing most human experts. These findings demonstrate the reliability of our method in clinical diagnosis.

![The papers of key laboratory teacher Luo Yuemei and graduate student Li Yuan were accepted by the journal Knowledge-Based Systems](https://imic.nuist.edu.cn/__local/C/82/FC/4C5702169BD4181EFB754DF9AD4_17CFA85E_65A8.png)

Figure 5 Comparison of accuracy between the method proposed in this paper and human experts

Summary

This paper proposes a semi-supervised learning method for retinal disease detection based on OCT images. The method combines the WideResNet network for feature extraction and learning of raw OCT images, and two innovative downstream modules: a prediction module and a comparison module. This paper designs a category-aware contrastive learning framework to trade off traditional supervised, semi-supervised and contrastive learning losses to avoid confirmation bias and improve model performance. Experimental results show that this method only requires 55, 102 and 80 labeled OCT images for training on the BOE, RetinalOCT and CELL data sets respectively, and the accuracy reaches 0.966, 0.964 and 0.957 respectively. This demonstrates the effectiveness of using OCT images to detect retinal diseases.

The research team of the Key Laboratory of Intelligent Medical Image Computing brings together experts and students from various fields such as medicine and engineering. With their respective professional backgrounds and knowledge, they work together to solve key problems in the medical industry. The interdisciplinary team structure of doctors and engineers allows them to integrate resources from different perspectives, promote the innovation and application of medical technology, thereby improving the efficiency and quality of diagnosis and treatment, and promoting the continuous development of the medical industry. This study demonstrates the potential of semi-supervised learning in retinal disease detection and provides a new direction for future research exploration. In this research work, by combining category-aware contrast learning with the FixMatch method, the researchers successfully achieved high-precision retinal disease recognition under extremely limited annotation data. This technology not only effectively reduces the workload of manual annotation, but also provides strong support for clinical diagnosis. With the accumulation of more data and the continuous emergence of more advanced algorithms, the field of intelligent medical image computing will continue to progress, promoting more breakthroughs and innovations in the medical industry.

---

*Translated from the [original Chinese source](https://imic.nuist.edu.cn/info/1032/1364.htm).*
