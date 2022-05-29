import pandas
import joblib

data = pandas.read_csv('SalaryData.csv')
Y = data["Salary"]
X = data["YearsExperience"]

X = X.values.reshape(-1,1)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X,Y)
print("-------------Model Created------------")
joblib.dump(model,'trained_model.pkl')
print("-------------Model Saved------------")
