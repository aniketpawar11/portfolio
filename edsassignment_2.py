# -*- coding: utf-8 -*-
"""edsassignment 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tIS9vo3pag4DU_3tOmUY1FgGEDglgwbF

<h2>Practice Lab Assignment:</h2>
1. Perform all List Operations, Tuple Operations, Dictionary Operations.
<br><h2>Lab Assignment:</h2>
<ul><li>Prepare/Take dataset for any real life application. For Ex. Sales of the company. </li><li>Read the data from
Sales.csv/.xls/.txt.</li> <li>Store Product details in List data structure. </li><li>Store Supplier Details in Dictionary
Data Structure.</li> <li>Store Customer Details in Tuple Data Structure. </li><li>Now perform the following operations:</li></ul><br>
- Find the most popular product for sales.<br>
- Find the best supplier for sales.<br>
- Find the customer who buys most of the products.<br>
- Find the number of customer who are ‘Female’<br>
<h2>Self Study Assignment:</h2> Consider the student result dataset. Find 10 grains for the student result.
For 10 grains find the solution using list, tuple and dictionary.
<font color="red"><h2>Prepared By: Nilesh B. Korade</h2></font>

# 1. Read CSV into python data structure
"""

Product_details=[]
Supplier_details=dict()
Customer_details=[]
gender={}

fp1=open("Sales.csv","r")
data=fp1.readline()

while(True):

    data=fp1.readline()
    if not data:
        break;
    #print(data)
    data=data.replace("\n","")
    temp=data.split(",")
    Product_details.append(temp[1])
    Customer_details.append(temp[3])
    Supplier_details.update({temp[0]:temp[2]})
    gender.update({temp[3]:temp[4]})

fp1.close()

Customer_details=tuple(Customer_details)
print(type(Customer_details))

print("\nProduct_details\n",Product_details,end="")
print("\n\nCustomer_details\n",Customer_details,end="")
print("\n\nSupplier_details\n",Supplier_details,end="")
print("\n\nGender_details\n",gender,end="")

"""# 2. Find the most popular product for sales."""

frequency = {}#{Lenovo Laptop:3}
# iterating over the list
for item in Product_details:
   # checking the element in dictionary
   if item in frequency:
      # incrementing the counter
      frequency[item] += 1
   else:
      # initializing the count
      frequency[item] = 1
# printing the frequency
print(frequency)
marklist = sorted(frequency.items(), key=lambda x:x[1],reverse=True)
sortdict = dict(marklist)
print(sortdict)
print("The most popular product for sales",list(sortdict.keys())[0]," sold ",list(sortdict.values())[0],"times")

"""<Center><h2>OR"""

# to install collections
pip install collections #shift+enter

from collections import Counter
counter = dict(Counter(Product_details))
sorted_counter = sorted(counter.items(), key=lambda x:x[1],reverse=True)
sorted_counter=dict(sorted_counter)
print("The most popular product for sales",list(sorted_counter.keys())[0],
      " sold ",list(sorted_counter.values())[0],"times")

"""# 3. Find the best supplier for sales"""

frequency = {}
# iterating over the list
for item in Supplier_details.values():
   # checking the element in dictionary
   if item in frequency:
      # incrementing the counter
      frequency[item] += 1
   else:
      # initializing the count
      frequency[item] = 1
# printing the frequency
print(frequency)
marklist = sorted(frequency.items(), key=lambda x:x[1],reverse=True)
sortdict = dict(marklist)
print(sortdict)
print("The most popular Supplier for sales",list(sortdict.keys())[0],
      " sold ",list(sortdict.values())[0],"Items")

"""<Center><h2>OR"""

from collections import Counter
counter = dict(Counter(list(Supplier_details.values())))
sorted_counter = sorted(counter.items(), key=lambda x:x[1],reverse=True)
sorted_counter=dict(sorted_counter)
print("The most popular Supplier for sales",list(sorted_counter.keys())[0],
      " sold ",list(sorted_counter.values())[0],"Items")

"""# 4. Find the customer who buys most of the products."""

frequency = {}
# iterating over the list
for item in Customer_details:
   # checking the element in dictionary
   if item in frequency:
      # incrementing the counter
      frequency[item] += 1
   else:
      # initializing the count
      frequency[item] = 1
# printing the frequency
print("Freqenct is as below:\n",frequency)
marklist = sorted(frequency.items(), key=lambda x:x[1],reverse=True)
sortdict = dict(marklist)
print("\nSorted dict is as below:\n",sortdict)
print("\n\nThe customer who buys most of the products",list(sortdict.keys())[0],
      " buy ",list(sortdict.values())[0],"Items")

"""<Center><h2>OR"""

from collections import Counter
counter = dict(Counter(Customer_details))
sorted_counter = sorted(counter.items(), key=lambda x:x[1],reverse=True)
sorted_counter=dict(sorted_counter)
print("The customer who buys most of the products",list(sorted_counter.keys())[0],
      " buy ",list(sorted_counter.values())[0],"Items")

"""# 5. Find the number of customer who are ‘Female’"""

# Identify Unique Customer
from collections import Counter
counter = dict(Counter(Customer_details))
names=list(counter.keys())
print(names)
male=0
female=0

for name in names:
    if gender[name]=="Male":
        male=male+1
    if gender[name]=="Female":
        female+=1
print("Total no of Male=",male)
print("Total no of Female=",female)