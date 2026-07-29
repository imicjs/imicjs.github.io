---
title: The paper of Professor Luo Yuemei’s research group from IMIC Lab was published
  in the international authoritative journal Applied Soft Computing
date: '2026-02-28T00:00:00+08:00'
summary: Recently, the team of teacher Luo Yuemei from Jiangsu University Key Laboratory
  of Intelligent Medical Image Computing (IMIC) at Nanjing University of Information
  Science & Technology published the latest research results in the internationally
  authoritative journal "Applied Soft Computing" in the field of engineering…
type: blog
categories:
- Comprehensive news
tags:
- IMIC
- News·Notifications
source_url: https://imic.nuist.edu.cn/info/1032/1495.htm
source_language: zh-CN
translation_status: machine-translated-and-terminology-normalized
---

Recently, the team of teacher Luo Yuemei from Jiangsu University Key Laboratory of Intelligent Medical Image Computing (IMIC) at Nanjing University of Information Science & Technology published the latest research results in the internationally authoritative journal "Applied Soft Computing" in the field of engineering technology and computer science.

The study is titled "Dual-channel cue-enhanced semi-supervised segmentation method for quantitative analysis of retinal blood vessels in OCTA images." This research is dedicated to solving the core pain points of retinal blood vessel segmentation in clinical OCTA images. Based on conventional non-invasive OCTA fundus images, it integrates the Segment Anything Model (SAM) basic large model prior and semi-supervised consistency learning technology to build an intelligent model that can achieve high-precision retinal blood vessel segmentation with only a very small amount of annotated data. The model (as shown in the figure) designed a full-process semi-supervised learning framework for OCTA images, and completed image standardization preprocessing and feature encoding before model training; the core architecture adopts a collaborative training mode of a shared image encoder and a dual-weighted decoder, integrating two segmentation paths of prompt guidance and no prompts to improve the generalization ability under a small amount of labeled data; for massive unlabeled data, a cross-prompting strategy is innovatively designed to eliminate unlabeled data. Pseudo cue points are generated in the prediction results of the data, and bidirectional supervision guidance is established between the dual decoder branches to fully mine the effective information of unlabeled data. At the same time, a cue consistency regularization strategy is introduced, combined with a mixed sampling scheme of center points and random points, to constrain the output stability of the model under different spatial cues, effectively alleviating the inherent defect of the SAM model being highly sensitive to the position of cue points, and finally achieving robust blood vessel segmentation in scenarios with scarce annotations. This model shows excellent segmentation performance in internal cross-validation of public data sets, and its comprehensive performance surpasses many current mainstream supervised learning and semi-supervised learning methods. In addition, through multiple sets of ablation experiments and visual analysis, the gain effect and model optimization logic of each core module were fully verified, further clarifying the application value of semi-supervised cue learning in medical image segmentation.

This technology has achieved a breakthrough in achieving high-precision retinal blood vessel segmentation using only 5% of the annotated data, significantly reducing the annotation cost and professional threshold of fundus image analysis, and effectively solving the core problem of scarcity of ophthalmic image annotation in clinical practice and reliance on the professional experience of doctors for annotation. Its excellent segmentation accuracy, blood vessel structure continuity and model robustness can provide stable and reliable technical support for quantitative analysis of retinal blood vessels. It is expected to significantly accelerate the clinical analysis process of OCTA images, assist ophthalmologists in completing early screening of eye diseases, longitudinal disease course monitoring and accurate prognosis assessment, and provide strong AI support for the precise diagnosis and treatment of eye diseases such as diabetic retinopathy, glaucoma and age-related macular degeneration.

![The paper of Professor Luo Yuemei’s research group from IMIC Lab was published in the international authoritative journal Applied Soft Computing](https://imic.nuist.edu.cn/__local/3/72/27/D6FFBE097EAF080142592C2E694_CF61D12D_2014E1.png)

Figure. Schematic diagram of the model framework proposed in this article.

Reference method and original link to this article

Yuemei Luo, Yuan Li, Lei Tao, Jun Xu, and Linbo Liu, Dual-path Prompt-enhanced Semi-supervised Segmentation for Retinal Vessel Quantification in OCTA Imaging, Applied Soft Computing, 2026:114778. https://doi.org/10.1016/j.asoc.2026.114778

---

*This page was translated from the [original Chinese source](https://imic.nuist.edu.cn/info/1032/1495.htm).*
