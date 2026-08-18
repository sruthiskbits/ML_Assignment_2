a.	Problem Statement
Binary classification of breast cancer tumors using the Breast Cancer Wisconsin (Diagnostic) dataset (UCI repository, 569 samples, 30 features).

b.	Dataset description
 The Breast Cancer Wisconsin (Diagnostic) dataset, obtained from the UCI Machine Learning Repository through the scikit-learn library, is a binary classification dataset used to predict whether a breast tumor is malignant or benign based on 30 numerical features extracted from fine needle aspirate (FNA) images. It contains 569 instances with no missing values. The target variable has two classes: 0 = Malignant and 1 = Benign, making it suitable for comparing multiple classification models.

c.	 Github Repository Link
https://github.com/sruthiskbits/ML_Assignment_2  
Streamlit app link
https://mlassignment2-bgvsbyyyvyzzrhzf39svxu.streamlit.app/ 

d.	Models Used
The following machine learning models were implemented and evaluated on the Breast Cancer Wisconsin (Diagnostic) dataset using Accuracy, AUC Score, Precision, Recall, F1 Score, and Matthews Correlation Coefficient (MCC).
Evaluation Metrics:
Model	Accuracy	AUC	Precision	Recall	F1	MCC
Logistic Regression	0.9825	0.9954	0.9861	0.9861	0.9861	0.9623
Decision Tree	0.9123	0.9157	0.9559	0.9028	0.9286	0.8174
kNN	0.9561	0.9788	0.9589	0.9722	0.9655	0.9054
Naive Bayes	0.9386	0.9878	0.9452	0.9583	0.9517	0.8676
Random Forest	0.9561	0.9937	0.9589	0.9722	0.9655	0.9054

e.	Observations on the performance of model
ML Model Name	Observation about model performance
Logistic Regression	Achieved the highest accuracy (98.25%) and AUC (99.54%), making it the most effective model for this dataset.
Decision Tree	Produced the lowest accuracy (91.23%) and MCC, indicating weaker generalization compared to the other models.
kNN	Performed well after feature scaling, achieving 95.61% accuracy with high recall and F1 score.
Naive Bayes	Delivered good AUC (98.78%) and recall while training quickly, though its accuracy was slightly lower than the top-performing models.
Random Forest (Ensemble)	Achieved strong overall performance with 95.61% accuracy and 99.37% AUC, providing balanced and reliable predictions.
Overall Winner for your dataset	Logistic Regression was the best-performing model because it achieved the highest accuracy, AUC, F1 score, and MCC on the test dataset.

