#random forest classifier
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,plot_confusion_matrix,f1_score,confusion_matrix
df=pd.read_csv('G:\Tech Topics\Data Science Course\DATA\Telco-Customer-Churn.csv')
X=df.drop(['customerID','Churn'],axis=1)
X=pd.get_dummies(X,drop_first=True)
y=df['Churn']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.10,random_state=101)
decision_tree=RandomForestClassifier()
param_grid={'max_depth':[1,3,5,6,8,10],'n_estimators':[1,5,10,25,50,100]}
grid_search_model=GridSearchCV(decision_tree,param_grid,scoring='accuracy')
grid_search_model.fit(X_train,y_train)
print(grid_search_model.best_params_)
y_pred=grid_search_model.predict(X_test)
print(accuracy_score(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))
plot_confusion_matrix(grid_search_model,X_test,y_test)
