import pandas as pd
import numpy as np

#Here check the first rows of the file 
df = pd.read_csv("Employee data set.csv")
print("\n")
print(df.head())
print("\n")
#checking the missing values

print("missing values in each column")
print(df.isnull().sum())
print("\n")

#checking the unique values in salary 
print("printing unique values in salary")
print(df["Salary(INR)"].unique())
print("\n")

#Need to convert the string array of salary(INR) col into the numeric

df["Salary(INR)"]= pd.to_numeric(df["Salary(INR)"],errors="coerce")

df["Salary(INR)"]=df["Salary(INR)"].fillna(df["Salary(INR)"].mean())

print(df["Salary(INR)"].head())
print("\n")

#calculating the middle value 
df["Age"] = np.where((df["Age"]>0) & (df["Age"]<=120) , df["Age"] , np.nan)  #here it change the invalid age and replace with nan
df["Age"] = df["Age"].fillna(df["Age"].median()) #fill nan with median 


df.replace([np.inf , -np.inf],np.nan,inplace=True)

#df.fillna(df.mean(), inplace=True)

#remove duplicate record
df.drop_duplicates(inplace=True)


#here we replaced negative salary  
df["Salary(INR)"] = np.where(df["Salary(INR)"]<0,df["Salary(INR)"].mean(),df["Salary(INR)"])

#salary should be have to be in limites like somewhere salary have in neg, in trilion or inf. so that is not valid 
salary_mean = df["Salary(INR)"].mean()
salary_std = df["Salary(INR)"].std()

lower_bound = salary_mean - (3*salary_std)
upper_bound = salary_mean + (3*salary_std)

#here we removed our salary rows where it tooo high and too low 
df= df[
    (df["Salary(INR)"]>=lower_bound) & 
    (df["Salary(INR)"]<=upper_bound)
]


#here is also few issue like in the other columns have none value or something else
#replacing the joining data
#convert covert column into datetimes
df["Joining_Date"] = pd.to_datetime(df["Joining_Date"], 
                                    format="mixed" , 
                                    errors="coerce") # here need to add format , because data format are different

#finding the average value 

df["Joining_Date"] = df["Joining_Date"].fillna(df["Joining_Date"].mean())
df["Joining_Date"] = df["Joining_Date"].dt.date  #dt.date  - use for remove the extra data of date 


#For Department , Name ,Email,city 

#check the null value in the Department , Name  , Email , city 
print("Display Null wise in the columns \n")
print(df[["Department" , "City" , "Name" , "Email"  ]].isnull().sum())

df[["Department" , "City" , "Name" , "Email" ]] = df[["Department" , "City" , "Name" , "Email" ]].fillna(
    df[["Department" , "City" , "Name" , "Email" ]].mode().iloc[0])

df.to_csv("final cleaned file.csv" , index = False)

print(" \n data cleaned Succefully \n ")


print("This is our final cleaned dataset \n" , df)