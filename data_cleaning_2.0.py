import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("For_practice.csv")
print(df.head(5))
print("\n")
print(df.tail(5))

print("\n")

print("length  : " , len(df))

print("find null numbers : ")
print(df.isnull().sum())
print("\n")

print("remove duplicates")

df = df.drop_duplicates()

print("repeat we check len" , len(df)) 

print("\n")
print(df.info())

print("\n")

print(df.describe())


print(df.columns)
print("\n \n")

print(df["Age"].info())
print("\n")
print(df["Age"].describe())
print("\n")

"""print("we dont want age in float so we convert into int")
df["Age"] = df["Age"].astype("Int64")"""

print("\n \n ")
print("\n" , df["Age"].info())
print("\n \n ")
print(df["Age"].head(10))


print("find the problem")
print(df["Age"].describe())

print("\n ")

#df["Age"] = np.where( (df["Age"]<0))


print(df["Age"] . describe())

#df["Age"] = np.where(df["Age"] < 0, np.nan, df["Age"])

df.loc[ df["Age"]>100 , "Age"] = np.nan
"""syntax = 

.loc[ rows , coumn ] = ValueError

"""

df.loc[df["Age"]<0 , "Age"] = np.nan

print(" Total Null Numbers : " , df["Age"].isnull().sum())


df["Age"] = df["Age"].fillna(df["Age"].mean())

print(" Total Null Numbers : " , df["Age"].isnull().sum())


print("\n ")
print("Total Positive Number : -  ",(df["Age"]>0).sum())
print("Total Negative Number : -  ",(df["Age"]<0).sum())
print("Total  Number : -  ",len(df["Age"]))

print("\n")


print(df["Age"].head())
print("\n \n ")

print("after cleaning Age Column : - \n " , df["Age"].describe() , "\n ")

#Next Move to the Gender 

print(df["Gender"].describe() )
print("data Type of Gender",df["Gender"].dtype)

print("\n")

print(df["Gender"].unique())

df["Gender"] = np.where(
    df["Gender"]=="Maal" , "Male" , df["Gender"]
)
df["Gender"] = df["Gender"].str.lower()
df["Gender"] = df["Gender"].str.capitalize()

print("After Cleaning : - " , df["Gender"].unique())

print("\n")


# Next Churn Column 

print(df["chur"].head(10))
print("Total Null Numbers : - ",df["chur"].isnull().sum())

print("Get Unique Values " , df["chur"].unique())


#Monthly charges 
print("\n ")
print(" data type of Monthly_Charges coln :- ", df["Monthly_Charges"].dtype )

print("Getting the Description of Monthly_Charges ")
print("\n")
print(df["Monthly_Charges"].describe())

print("\n" , df["Monthly_Charges"].info(), "\n")


df["Monthly_Charges"] = np.where(
    (df["Monthly_Charges"]<0) | (df["Monthly_Charges"]>=5000) , np.nan , df["Monthly_Charges"]
)


print("\n  Again get desciption to reconfirm :-  " ,  df["Monthly_Charges"].describe())

df["Monthly_Charges"] = df["Monthly_Charges"].fillna(np.random.randint(
    1 , 1000
)
)
print("\n ")

print("Monthly Charges Converted into int and get 5 rows : - ")
df["Monthly_Charges"] = df["Monthly_Charges"].astype(int)
print(df["Monthly_Charges"].head(5))


print("\n ")

print(df["Monthly_Charges"].info())
print("\n " , df["Monthly_Charges"].describe())



# Payment Method col
print("\n")
print(df["Payment_Method"].unique())
print(" Total Null Number Of Payment_Method : ",df["Payment_Method"].isnull().sum())

df["Payment_Method"] = df["Payment_Method"].fillna(df["Payment_Method"].mode().loc[0])

print("Number Of UPI payment Method :- ",(df["Payment_Method"]=="UPI").sum())
print("Number Of Credit Card : - " , (df["Payment_Method"]=="Credit Card").sum())
print("Number Of Electronic Check :- ", (df["Payment_Method"]=="Electronic check").sum())
print("Numer Of BANK Transfer Method : " , (df["Payment_Method"]=="Bank Transfer").sum())



# Tenure Columns 

print(" \n Know The details About Tenure Columns ")
print(df["Tenure"].info())
print("\n " , df["Tenure"].describe())

df.loc[df["Tenure"]>50 , "Tenure"] = np.nan
df["Tenure"] = df["Tenure"].fillna(df["Tenure"].mean())
print("\n  Tenure Nulls elements : -  " , df["Tenure"].isnull().sum())


print("After Done . The Desciption Of Tenure Columns : " , df["Tenure"].describe())

print(df.columns)



#Internet Serivice 
print("\n")
print(df["Internet_Service"].info())

print("\n",df["Internet_Service"].head(10))
print(" \n  Unique Element's in The Internet Services :- ",df["Internet_Service"].unique())
print("\n")


df["Internet_Service"] = df["Internet_Service"].fillna(df["Internet_Service"].mode().loc[0])

print("Null Numbers IN Inernet Serivices Column  : - " , df["Internet_Service"].isnull().sum())
print("\n after Cleaning , The Unique Members - " , df["Internet_Service"].unique())



#Contract 
print("\n ")
print(df["contract"].info()) 
print("\n ")
print(df["contract"].unique())

df["contract"] = df["contract"].str.lower()
print(df["contract"].unique())

df["contract"] = df["contract"].str.capitalize()
print(df["contract"].unique())



print("\n \n Successfully Cleaned Employee Dataset  \n ")



Gender = df["Gender"].value_counts()
plt.pie(Gender , labels= Gender.index , autopct= "%1.1f%%" , startangle=90 )
plt.savefig("Data_Cleaning-Gender.png")
plt.title(" Employee Gender " , color= "red")
plt.tight_layout()
plt.show()

Payment_method = df["Payment_Method"].value_counts()
plt.pie(Payment_method , labels= Payment_method.index , autopct= "%1.1f%%" , startangle=90)
plt.title("Payments Method " , color="black" , size =30 )
plt.tight_layout()
plt.savefig("Data_Cleaning-Payment_Method.png")
plt.show() 

churn = df["chur"].value_counts()
plt.barh(churn.index , churn.values , color = 'purple')
plt.xlabel("Number of Employee")
plt.ylabel("YES OR NO")
plt.title("Churn DATA")
plt.grid(color = "gray")
plt.tight_layout()
plt.savefig("Data_Cleaning-churn.png")
plt.show()

