# Evaluating Missing Data Imputation Methods for Machine Learning

## Aim

This project investigates how different missing-data imputation methods affect the performance of machine learning models. Starting from complete datasets, missing values will be artificially introduced under controlled settings, allowing different imputation strategies to be compared.

The goal is to compare classical and Bayesian approaches for handling missing values while developing practical experience with Bayesian inference and probabilistic machine learning techniques.

## Motivation and Background

Missing values are a common challenge in machine learning and statistical analysis, particularly in areas such as healthcare, finance, and scientific research. Poor handling of missing data can reduce the accuracy, reliability, and interpretability of machine learning models.

The impact of missing data depends on the mechanism causing the missingness, commonly categorised as:

- Missing Completely At Random (MCAR)
- Missing At Random (MAR)
- Missing Not At Random (MNAR)

Different approaches exist for handling missing values, ranging from simple statistical imputation methods to probabilistic approaches that explicitly model uncertainty.

This project investigates how different imputation strategies influence downstream machine learning performance, with particular interest in whether Bayesian approaches provide advantages by modelling uncertainty.

## Project Scope

This is an exploratory summer project designed to build practical experience in missing-data handling, machine learning evaluation, and Bayesian modelling.

The project aims to develop the theoretical and practical foundations required for future work involving Bayesian approaches to learning from incomplete datasets.

## Research Questions

This project aims to answer:

- How much does the choice of imputation method affect machine learning performance?
- Which imputation methods perform best as the percentage of missing data increases?
- How do Bayesian approaches compare with classical imputation methods in terms of predictive performance and uncertainty estimation?
- Which methods are most robust under different levels of missingness?
- Do some machine learning models handle imperfect imputations better than others?

## Experimental Design

The project evaluates how different missing-data handling approaches influence machine learning performance.

The experimental workflow is:

1. Begin with a complete dataset.

2. Introduce missing values artificially at controlled missingness levels:
   - 10% missing data
   - 20% missing data
   - 30% missing data
   - 50% missing data

3. Apply different missing-data handling strategies, progressing from simple statistical methods to more advanced approaches:
   - Complete-case analysis
   - Mean/median imputation
   - KNN imputation
   - MICE
   - Bayesian approaches

4. Train fixed machine learning models:
   - Logistic Regression
   - Random Forest

5. Evaluate model performance using:
   - Accuracy
   - F1-score
   - AUC
   - Measures of uncertainty where applicable

6. Compare how different approaches perform as missingness increases.

The dataset, machine learning models, and evaluation metrics will remain fixed while the missing-data handling method is varied. This provides a controlled framework for comparing different approaches.

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

More advanced approaches:

- K-nearest neighbours (KNN) imputation
- Multiple Imputation by Chained Equations (MICE)

These methods consider relationships between variables and attempt to better represent the underlying data distribution.

### Bayesian Methods

The project will explore Bayesian approaches to missing data to investigate how probabilistic modelling can represent uncertainty when estimating missing values.

Possible approaches include:

- Bayesian linear regression as an introduction to Bayesian modelling.
- Bayesian imputation models.
- Posterior sampling using probabilistic programming frameworks such as PyMC.

The final Bayesian approach will be selected based on the theoretical understanding and practical experience developed during the project.

## Machine Learning Models

The following models will be used to evaluate the impact of imputation methods:

- Logistic Regression
- Random Forest

## Evaluation Metrics

Evaluation metrics will include:

- Accuracy
- F1-score
- AUC
- Prediction uncertainty (where applicable)

## Tools and Libraries

Currently used:

- Python
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Missingno

Planned:

- ArviZ
- PyMC

## Results

## Future Work

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

## Current Progress

## Week 1: Setup and Exploratory Data Analysis

Completed:
- Created project structure and development environment.
- Selected the Breast Cancer Wisconsin dataset.
- Performed exploratory data analysis.
- Investigated dataset structure, distributions, correlations, and missing values.

## Week 2: Baseline Machine Learning Models

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

Next:
- Investigate more advanced imputation approaches, including MICE.
- Begin exploring Bayesian approaches to missing data.

## References
