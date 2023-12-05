# Regression Analysis of Mohs Hardness Data Using Bayesian Network Hyperparameter Optimization

The Mohs Hardness scale rates the hardness of different minerals. The data used here combine both real data from mineral data and crystal data as well as a dataset generated using a deep learning model. The process that we have employed to predict the Mohs Hardness value uses different machine learning models: Random Forest, XGBoost, Light GMBoost. To optimize the parameters of each of these models, we used two different optimizers, Bayesian and Optuna, and evaluated our outcomes based on the Median Absolute Error.  

This project was part of the Kaggle Playground Series - Season 3, Episode 25 [Regression with a Mohs Hardness Dataset](https://www.kaggle.com/competitions/playground-series-s3e25). 

[My contribution](https://www.kaggle.com/code/freshoats/mohs-regression-with-random-forest-and-bayes-opt) used a Random Forest Regressor, XGBoost Regressor and Light GBM Regressor, all optimizing the hyperparameters with Bayesian Network Cross Validation. 