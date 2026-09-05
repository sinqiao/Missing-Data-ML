# Evaluating Missing Data Imputation Methods for Machine Learning

## Project Status
**Completed - exploratory study**

This project investigated the effect of missing data and classical imputation methods on downstream machine-learning performance. Missing values were artificially introduced under MCAR at varying rates, and complete-case analysis, mean/median imputation, and KNN imputation were evaluated using Logistic Regression and Random Forest models.

Particular attention was given to KNN imputation and the effect of feature scaling on distance-based neighbour selection, with preprocessing and data-leakage considerations incorporated into the experimental pipeline.

The project provides a practical foundation for future investigation of multiple-imputation and probabilistic/Bayesian approaches to missing data.


## Aim

This project investigates how missing data and different imputation methods affect the performance of machine learning models. Starting from a complete dataset, missing values are artificially introduced under controlled conditions, allowing different missing-data handling strategies to be compared.

The project focuses on classical imputation methods, including complete-case analysis, mean/median imputation, and K-nearest neighbours (KNN) imputation. Particular attention is given to the effect of preprocessing choices on KNN imputation and downstream machine learning performance.

The aim is to develop practical experience with missing-data handling and machine learning evaluation, while building a foundation for future investigation of probabilistic and Bayesian approaches to incomplete data.

## Motivation and Background

Missing values are a common challenge in machine learning and statistical analysis, particularly in areas such as healthcare, finance, and scientific research. Poor handling of missing data can reduce the accuracy, reliability, and interpretability of machine learning models.

The impact of missing data depends on the mechanism causing the missingness, commonly categorised as:

- Missing Completely At Random (MCAR)
- Missing At Random (MAR)
- Missing Not At Random (MNAR)

Different approaches exist for handling missing values, ranging from simple statistical imputation to methods that exploit relationships between variables or explicitly model uncertainty.

This project focuses on the effects of classical imputation methods under controlled MCAR missingness. By comparing different approaches across increasing levels of missingness and evaluating their effect on downstream machine learning models, the project provides a practical introduction to the challenges involved in learning from incomplete data.

The limitations of classical imputation methods, particularly their treatment of uncertainty, also motivate future investigation of multiple-imputation and Bayesian approaches.

## Project Scope

This is an exploratory summer project designed to build practical experience in missing-data handling and machine learning evaluation.

The completed study focuses on MCAR missingness and classical imputation methods, including complete-case analysis, mean/median imputation, and KNN imputation. Logistic Regression and Random Forest are used as fixed downstream models to evaluate the effects of different missing-data handling strategies.

More advanced approaches, including MICE and Bayesian imputation, are outside the scope of the completed study and are identified as potential directions for future work.

## Research Questions

This project aims to answer:

- How does the level of missing data affect machine-learning performance?
- How does the choice of classical imputation method affect model performance?
- How does KNN preprocessing, particularly feature scaling, affect imputation and downstream model performance?
- Are some machine-learning models more robust to missing data and imputation than others?

Future research: How do multiple-imputation and Bayesian approaches compare with classical methods, particularly in their treatment of uncertainty?

## Experimental Design

The project evaluates how different missing-data handling approaches influence machine learning performance.

The experimental workflow is:

1. Begin with a complete dataset.

2. Introduce missing values artificially at controlled missingness levels:
   - 10% missing data
   - 20% missing data
   - 30% missing data
   - 50% missing data

3. Apply different missing-data handling strategies:
   - Complete-case analysis
   - Mean imputation
   - Median imputation 
   - KNN imputation
   For KNN imputation, the effect of feature scaling and preprocessing is also investigated.

4. Train fixed machine learning models:
   - Logistic Regression
   - Random Forest

5. Evaluate model performance using:
   - Accuracy
   - F1-score
   - ROC-AUC

6. Compare how different approaches perform as missingness increases.

The dataset, machine learning models, and evaluation metrics are kept fixed while the missing-data handling method is varied. This provides a controlled framework for investigating the effect of missingness and classical imputation strategies on downstream machine learning performance.

## Dataset

Dataset:
Breast Cancer Wisconsin Dataset

Source:
scikit-learn

## Imputation Methods
### Baseline Methods

The initial baselines are:

- Complete-case analysis
- Mean imputation
- Median imputation

### Classical Methods

The project then considers K-nearest neighbours (KNN) imputation as a more data-driven approach that uses relationships between observations to estimate missing values.

- K-nearest neighbours (KNN) imputation

Particular attention is given to the effect of feature scaling on KNN neighbour selection, since KNN relies on distances between observations.

## Machine Learning Models

ML models used to evaluate the impact of imputation methods:

- Logistic Regression
- Random Forest

## Evaluation Metrics

Evaluation metrics included:

- Accuracy
- F1-score
- ROC-AUC

## Tools and Libraries
- Python
- NumPy
- Pandas
- Scikit-learn
- Matplotlib

## Results

The experiments showed that increasing MCAR missingness generally reduced downstream predictive performance, with the effect becoming more noticeable at higher missingness levels.

Key findings:
- KNN imputation achieved the highest mean ROC-AUC among the tested imputation methods at every missingness level for both Logistic Regression and Random Forest.
- The advantage of KNN was relatively small at lower missingness levels but became more noticeable at 50% missingness, particularly for Random Forest.
- Logistic Regression remained relatively robust to increasing missingness. At 50% missingness, KNN-imputed data achieved an ROC-AUC of 0.9910, compared with 0.9954 on complete data.
- Random Forest showed a slightly larger reduction in ROC-AUC, from 0.9937 on complete data to 0.9881 with KNN imputation at 50% missingness.
- Complete-case analysis resulted in substantial data loss. At 10% missingness, only approximately 20 training observations remained on average, compared with 455 observations with imputation. As missingness increased, too few complete observations remained for meaningful evaluation, so higher missingness levels were not tested.

Overall, the results suggest that the choice of missing-data handling method can affect downstream model performance, while simply discarding incomplete observations can result in substantial data loss.

## Future Work

Several extensions were identified but were outside the scope of the completed exploratory study.

### Multiple Imputation

Multiple Imputation by Chained Equations (MICE) could be investigated as an extension to the classical methods considered in this project. Unlike single imputation, multiple imputation can represent uncertainty by generating multiple plausible completed datasets.

### Bayesian Imputation

Bayesian approaches provide a potential direction for explicitly modelling uncertainty in missing values. Possible extensions include:

Bayesian linear regression as an introduction to Bayesian modelling
Bayesian imputation models
Posterior sampling using probabilistic programming frameworks such as PyMC

These approaches could be investigated in future work, particularly in the context of learning from incomplete datasets.

## Project Timeline

### Week 1: Setup and Exploratory Data Analysis

Completed:
- Created project structure and development environment.
- Selected the Breast Cancer Wisconsin dataset.
- Performed exploratory data analysis.
- Investigated dataset structure, distributions, correlations, and missing values.

### Week 2: Baseline Machine Learning Models

Completed:
- Prepared features (`X`) and target (`y`).
- Created a stratified 80/20 train/test split.
- Implemented Logistic Regression with feature scaling using a pipeline.
- Implemented Random Forest classification.
- Created an evaluation function using accuracy, F1-score, and ROC-AUC.
- Saved baseline model results to `results/baseline_results.csv`.

### Week 3: Missingness Simulation

Completed:
- Implemented controlled MCAR missingness.
- Tested missingness levels of 10%, 20%, 30%, and 50%.
- Verified the resulting missingness levels.
- Evaluated the effect of missingness on Logistic Regression and Random Forest.
- Established complete-case analysis as a baseline.

### Week 4: Classical Imputation

Completed:
- Implemented mean and median imputation.
- Implemented KNN imputation.
- Considered data leakage during preprocessing.
- Compared imputation methods under different levels of MCAR missingness.
- Evaluated Logistic Regression and Random Forest performance.

### Week 5: Validation of Classical Imputation

Completed:
- Investigated the effect of feature scaling on KNN neighbour selection.
- Reviewed the KNN preprocessing pipeline for potential methodological issues.
- Evaluated alternative preprocessing strategies.
- Re-ran the KNN experiments using the validated approach.
- Re-evaluated classical imputation methods under MCAR missingness.

## Repository Structure
Missing-Data-ML/
│
├── data/
├── figures/
├── notebooks/
├── results/
├── report/
├── src/
├── README.md
└── requirements.txt
