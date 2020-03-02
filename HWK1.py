'''
Programming for Business Intelligence and Analytics
PBIA HWK1
'''
"""
1) Compute and print both roots of the quadratic equation x^2 – 5.86 x + 8.5408.
"""
import math
#Accepting the coefficient values for the equation x^2 – 5.86 x + 8.5408
a = float(input("Enter the coefficient a:"))
b = float(input("Enter the coefficient b:"))
c = float(input("Enter the coefficient c:"))
#Classifying the tyoe of roots
beta = (b**2)-(4*a*c)
if beta == 0:
 print("Real and equal roots")
 root1 = (-b+math.sqrt(beta))/(2*a)
 print("Roots are ",root1," and ",root1)
elif beta> 0:
 print("Real and unequal roots")
 #Calculating the roots using the formula -b+sqrt(b^2-4ac)/2a and -b-sqrt(b^2-4ac)/2a
 root1 = (-b+math.sqrt(beta))/(2*a)
 root2 = (-b-math.sqrt(beta))/(2*a)
 print("Roots are ",root1," and ",root2)
else:
 print("Imaginary roots")

#  ~~~~~~~~~~~~~~~OUTPUT~~~~~~~~~~~~~~~
# Enter the coefficient a:1
# Enter the coefficient b:-5.86
# Enter the coefficient c:8.5408
# Real and unequal roots
# Roots are 3.1400000000000006 and 2.7199999999999998

"""
Use a for loop to print the decimal representations of 1/2, 1/3, ..., 1/10, one on each line.
"""
#Range is from 2 to 11 where the loop iterates for 10 times displaying the decimal representation of the values
for i in range(2,11):
 print(1/i) #prints the decimal values

# ~~~~~~~~~~~~~~~OUTPUT~~~~~~~~~~~~~~~
# 0.5
# 0.3333333333333333
# 0.25
# 0.2
# 0.16666666666666666
# 0.14285714285714285
# 0.125
# 0.1111111111111111
# 0.1

"""
2) Use a for loop to compute the 10th triangular number. The nth triangular number is
defined as
1+2+3+...+n.
(You can also compute the nth triangular number as n*(n+1)/2. Use this formula to
doublecheck that your loop is correct.)
Hint: This outline is an almost-complete solution. You only must replace each ellipsis by an
expression.
"""
n=10 #Obtain the value for n
triangular = 0 #Initializing the variable to 0
for i in range(0,n+1): #Simple for loop
 triangular = triangular + i #To calculate the triangular number by using for-loop
print("Triangular number", n, "using loop:", triangular)
print("Triangular number", n, "using formula:", int(n*(n+1)/2)) #Verifying using the formula

# ~~~~~~~~~~~~~~~OUTPUT~~~~~~~~~~~~~~~
# Triangular number 10 using loop: 55
# Triangular number 10 using formula: 55

"""
3) Use a for loop to compute 10! (the factorial of 10). Recall that the factorial of n is
1*2*3*...*n.
The first line of your solution will be n = 10. After that, your solution should not use 10 again,
though your solution will use n. In other words, your code (after the n = 10 line) should work
for
any value of n.
Hint: Your answer will be like your answer to "Problem 3: Triangular numbers".
"""

n=10 #Number whose factorial is to be calculated
factorial = 1 #Initializing to 1 as factorial of 0 is also 1
for i in range(1,n+1): #simple for loop declaration
 factorial = factorial * i #Calculating the factorial using simple for loop
print( "Factorial of",n, "is:", factorial) #Printing the value


# ~~~~~~~~~~~~~~~OUTPUT~~~~~~~~~~~~~~~
# Factorial of 10 is: 3628800

"""
4) Write code to print the first 10 factorials, in reverse order. In other words, write code that
prints
10!, then prints 9!, then prints 8!, ..., then prints 1!.
The first line of your solution should assign a variable numlines to 10, and then the rest of
your solution must not use 10 anywhere. Hint: Use two nested for loops.
"""
n=10
for j in range(n,0,-1): #Reverse for loop to display in reverse order
 factorial = 1 #Initializing to 1 as factorial of 0 is also 1
 for i in range(1,j+1): #Loop to calculate factorial of the numbers
 factorial = factorial * i #Calculate the factorial
 print( j,"! :",factorial)

# ~~~~~~~~~~~~~~~OUTPUT~~~~~~~~~~~~~~~
# 10 ! : 3628800
# 9 ! : 362880
# 8 ! : 40320
# 7 ! : 5040
# 6 ! : 720
# 5 ! : 120
# 4 ! : 24
# 3 ! : 6
# 2 ! : 2
# 1 ! : 1

"""
5) Compute the following value:
1 + 1/1! + 1/2! + 1/3! + 1/4! + ... + 1/10!
The value should be close to e (≈ 2.71828), the base of the natural logarithms
Hint: The easiest way to solve this is with two nested for loops. It is possible, but tricky, to
compute this using only one for loop. That is not necessary for this assignment. Hint: Copy
your solution to "Problem 5: Multiple factorials", then modify it. Rather than printing the
factorials, you will add their reciprocals to a running total, then print that total at the end.
Hint: don't try to work the very first "1 +" into your loop; do it outside the loops (either at the
very beginning or the very end of the outer loop).
"""

total = 1 #Initializing total to 1 to which the fractions are added
n=10
for j in range(n,0,-1): #Reverse for loop
 factorial = 1 #Initializing to 1 as factorial of 0 is also 1
 for i in range(1,j+1): #Loop to calculate factorial of the numbers
 factorial = factorial * i #Calculate the factorial
 total = total + 1/factorial #Adding the reciprocal of factorial to the total
print(total)

# ~~~~~~~~~~~~~~~OUTPUT~~~~~~~~~~~~~~~
# 2.718281801146385

“””
6. Part A: NOT GRADED: import the MS Excel Worksheet Sample_01 to Python. Do all sort of
statistics and graphs.
“””
import pandas as pd
#Extract the data from excel file and store in data
data = pd.read_excel(r'/Users/radhikakerur/PycharmProjects/Class1/Sample_01.xlsx')
print(data)
#Count the NAs in the dataset
print(data.isna().sum())
#Drop the unused data columns
data = data.drop(columns=["Customer_ID","First_Name_Customer","SSN"])
print(data.head())
#Replace the NAs with mean values for numeric values and NaN for categorical variables (Data
Cleaning process
data["Prop_01"].fillna(data["Prop_01"].mean(),inplace=True)
data["Prop_02"].fillna(data["Prop_02"].mean(),inplace=True)
data["Prop_03"].fillna(data["Prop_03"].mean(),inplace=True)
data["Prop_05"].fillna(data["Prop_05"].mean(),inplace=True)
data["Prop_07"].fillna(data["Prop_07"].mean(),inplace=True)
data["Prop_04"].fillna("NaN",inplace=True)
data["Prop_06"].fillna("NaN",inplace=True)
print(data.isna().sum())
#Summary Statistics
print(data.describe())
%matplotlib inline
#Frequency distribution for Prop_06
ax = data["Prop_06"].value_counts().plot(kind='bar')
#Frequency distribution for Prop_04
ax = data["Prop_04"].value_counts().plot(kind='barh')
#Boxplot to understand Account_Bal distribution
ax = data["Account_Bal"].plot(kind='box')
#Histogram for Prop_02 
ax = data["Prop_02"].plot(kind='hist')
#Scatterplot for Account_Bal and Prop_03
ax = data.plot.scatter(x = "Account_Bal", y = "Prop_03")
#Boxplot to identify any anamolies
ax = data["Prop_03"].plot(kind='box')

