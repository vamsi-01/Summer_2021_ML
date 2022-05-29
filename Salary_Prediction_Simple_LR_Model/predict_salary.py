import joblib

trained_model = joblib.load('trained_model.pkl')
print("---------------------------------------")
exp = input("Enter Your Experience: ")
print("---------------------------------------")
salary = trained_model.predict([[float(exp)]])

print("Your Expected Salary :{}".format(salary))
print("---------------------------------------")
