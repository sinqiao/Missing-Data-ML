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
- How do Bayesian imputation methods compare with classical approaches in terms of predictive performance and uncertainty estimation?
- Which methods are most robust under different levels of missingness?
- Do some machine learning models handle imperfect imputations better than others?

## Experimental Design

The project will evaluate how different missing-data handling approaches influence machine learning performance.

The experimental workflow is:

1. Begin with a complete dataset.

2. Introduce missing values artificially at controlled missingness levels:
   - 10% missing data
   - 20% missing data
   - 30% missing data
   - 50% missing data

3. Apply different imputation strategies:
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

6. Compare how different imputation methods perform as missingness increases.

The machine learning models, dataset, and evaluation metrics will remain fixed while the imputation method is varied. This allows the effect of missing-data handling strategies to be isolated and compared fairly.

## Dataset

Dataset:
Breast Cancer Wisconsin Dataset

Source:
scikit-learn

## Imputation Methods

### Baseline Methods

Simple statistical approaches:

- Mean imputation
- Median imputation

These methods provide a baseline and help understand their limitations and situations where they may still be appropriate.

### Classical Methods

More advanced approaches:

- K-nearest neighbours (KNN) imputation
- Multiple Imputation by Chained Equations (MICE)

These methods consider relationships between variables and attempt to better represent the underlying data distribution.

### Bayesian Methods

A Bayesian approach will be explored to understand how probabilistic models can represent uncertainty when estimating missing values.

Possible approaches include:

- Bayesian linear regression to develop understanding of Bayesian modelling.
- Bayesian imputation methods.
- Posterior sampling methods using probabilistic programming frameworks such as PyMC.

The exact Bayesian approach will be refined based on understanding gained during the project.

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

Python libraries used:

- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Missingno
- ArviZ
- PyMC (optional)

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

Next steps:
- Implement baseline machine learning models.
- Learn evaluation methodology.
- Introduce artificial missingness into the dataset.

## References
