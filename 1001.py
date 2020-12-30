import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import seaborn as sea
income=pd.read_csv('insurance.csv')
for_male=income[income['sex']=='male']
for_female=income[income['sex']=='female']
#print(for_male)
#print(income.info())
male_input=for_male['age']
male_input=np.array(male_input)
male_input=male_input.reshape(-1,1)
#print(x)
male_output=for_male['charges']
male_output=np.array(male_output)
female_input=for_female['age']
female_input=np.array(female_input)
female_input=female_input.reshape(-1,1)
female_output=for_female['charges']
female_output=np.array(female_output)
#plt.scatter(x,y)
#plt.show()
from sklearn.linear_model import LinearRegression
model1=LinearRegression()
model2=LinearRegression()
model1.fit(male_input,male_output)
model2.fit(female_input,female_output)
print('1 for male and 2 for female')
var1=input('enter your sex:')
var2=int(input('enter your age:'))
if var1==1:
    t=model1.predict([[var2]])
    print(f'if your age is {var2} and you are a male you will get an insurence cover of {t}')
else:
    f=model2.predict([[var2]])
    print(f'if your age is {var2} and you are a female you will get an insurence cover of {f}')
print(model1.coef_)
print(model1.intercept_)
print(model2.coef_)
print(model2.intercept_)