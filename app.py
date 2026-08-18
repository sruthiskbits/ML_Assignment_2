import streamlit as st, pandas as pd, joblib, os
st.title("ML Assignment 2 - by Sruthi S Kumar")
df=st.file_uploader("Upload Test CSV",type="csv")
model_name=st.selectbox("Model",["Logistic Regression","Decision Tree","kNN","Naive Bayes","Random Forest"])
if df:
 d=pd.read_csv(df)
 X=d.drop("target",axis=1)
 y=d["target"]
 p={"Logistic Regression":"Logistic_Regression.pkl","Decision Tree":"Decision_Tree.pkl","kNN":"kNN.pkl","Naive Bayes":"Naive_Bayes.pkl","Random Forest":"Random_Forest.pkl"}
 m=joblib.load(os.path.join("model",p[model_name]))
 pred=m.predict(X)
 prob=m.predict_proba(X)[:,1]
 from sklearn.metrics import accuracy_score,roc_auc_score,precision_score,recall_score,f1_score,matthews_corrcoef,confusion_matrix
 st.write({"Accuracy":accuracy_score(y,pred),"AUC":roc_auc_score(y,prob),"Precision":precision_score(y,pred),"Recall":recall_score(y,pred),"F1":f1_score(y,pred),"MCC":matthews_corrcoef(y,pred)})
 st.write("Confusion Matrix")
 st.write(confusion_matrix(y,pred))
