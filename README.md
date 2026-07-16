# Evaluating Missing Data Imputation Methods for Machine Learning

## Aim

This project investigates how different missing-data imputation methods affect the performance of machine learning models. The goal is to compare classical and Bayesian approaches for handling missing values, while developing practical experience with Bayesian inference and probabilistic machine learning techniques.

## Motivation

Missing values are common in real-world datasets, particularly in areas such as healthcare, finance, and scientific research. Poor handling of missing data can reduce the accuracy, reliability, and interpretability of machine learning models.

This project explores how the choice of imputation method influences downstream machine learning performance. In particular, it investigates whether more advanced approaches, such as Bayesian imputation, provide advantages over traditional methods by naturally modelling uncertainty.

## Project Scope

This is a summer research project designed to build practical experience in missing-data handling, machine learning evaluation, and Bayesian modelling. The project will provide background knowledge and experimental experience that may inform future research directions.

## Research Questions

This project aims to answer:

- How much does the choice of imputation method affect machine learning performance?
- Which imputation methods perform best as the percentage of missing data increases?
- Do Bayesian imputation methods outperform classical approaches?
- Which methods are most robust under different levels of missingness?
- Do some machine learning models handle imperfect imputations better than others?

## Experimental Design

The project follows this workflow:

1. Begin with a complete dataset.
2. Artificially introduce missing values at different levels:
   - 10% missing data
   - 20% missing data
   - 30% missing data
   - 50% missing data
3. Apply different missing-data imputation methods.
4. Train the same machine learning models on each completed dataset.
5. Compare model performance and uncertainty.

The machine learning models will remain fixed while the imputation methods are varied, allowing the impact of missing-data handling techniques to be evaluated fairly.

## Dataset

The project will use one or two structured/tabular datasets, such as healthcare, housing, or classification datasets.

The dataset will initially contain complete values, after which missingness will be artificially introduced to allow controlled comparisons.

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

Bayesian approaches will be explored to understand how probabilistic modelling can represent uncertainty in missing data:

- Bayesian linear regression
- Bayesian imputation approaches
- Posterior sampling methods (where appropriate)

Existing libraries will be used where possible.

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

## Project Status

Currently setting up the environment and preparing the experimental framework.