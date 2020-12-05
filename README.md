# Wine_Quality_Prediction

## Introduction

The dataset is related to the red variant of the Portuguese wine and it is retrieved from the UCI machine learning repository- 1.	https://archive.ics.uci.edu/ml/datasets/wine+quality . This is a public repository where the data is publicly available. It is a dataset about red wine and contains the chemical characteristics of the wine and quality is associated to it. This dataset can be viewed as a classification or regression task. There are different quality levels hence I will be performing regression and dividing the category into two major category and perform regression task. I will be analyzing different factors which help in improving the wine quality and accommodate companies to improve the marketing strategy. By predicting which factors plays an important role in the quality of wine companies can adjust their prices accordingly. It will also help in understanding what key factors makes the wine better as compared to other wines. In this dataset, I have classified wine qualities into 2 major categories as good and bad according to the quality levels for classifying the quality into two major categories I have considered that the quality above 6.5 is good and below that is bad. For prediction, I have used Logistic Regression, Naive Bayes, and Decision Tree models. 

## DATASET
There are 12 features in the dataset which contains the information about the acids, pH levels, alcohol volume, sugar and quality of the wine.
Input Variables:
•	fixed acidity: most acids involved with wine or fixed or non-volatile
•	volatile acidity: the amount of acetic acid in wine
•	citric acid: found in small quantities, citric acid is used for adding flavor and freshness to the wine 
•	residual sugar: the amount of sugar remaining after fermentation stops
•	chlorides: the amount of salt in the wine
•	free sulfur dioxide: the free form of SO2 exists in equilibrium between molecular SO2 (as a dissolved gas) and bisulfite ion
•	total sulfur dioxide: the amount of free and bound forms of S02
•	density: the density of water is close to that of water depending on the percent alcohol and sugar content
•	pH: describes how acidic or basic a wine is on a scale from 0 (very acidic) to 14 (very basic)
•	sulphates: a wine additive which can contribute to sulfur dioxide gas (S02) levels
•	alcohol: the percent alcohol content of the wine
Output Variable:
•	quality: output variable (based on sensory data, the score between 0 and 10)
For predicting the wine quality, the attribute quality will become our label and the rest of the attributes will become the features.



## CONCLUSION 
Among all the model's Decision Tree Classifier was a good fir for predicting the quality of the wine. Random Forest classifier can also be considered in the future as the Decision tree classifier yield good accuracy.
We can also observe that the False Negative is the least for Decision Tree Classifier and it made a good prediction.
Accuracy on Training Set and Test Set and it can be observed that Decision Tree classifier was a good model for both the cases.

