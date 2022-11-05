import re
import collections
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("iris.csv")
print("Bai 1.1)")
X_lebal = df.get('sepal_length')
Y_lebal = df.get('sepal_width')
fig = plt.figure(figsize=(10, 7))
plt.scatter(X_lebal, Y_lebal)
plt.title("Sepal")
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')
plt.show()

print("Bai 1.2)")
plt.figure(figsize=(10, 7))
plt.hist(X_lebal, bins=20, color="green")
plt.title("Sepal Length")
plt.xlabel("Sepal_Length")
plt.ylabel("Count")
plt.show()


df = pd.read_csv("company-sales_data.csv")
month = df.get('month_number')
total_profit = df.get('total_profit')
print("Bai 2.1)")
plt.figure(figsize=(13, 7))
plt.plot(month, total_profit, 'r')
plt.title("Total Profit per month")
plt.xlabel("Month")
plt.ylabel("profit")
plt.show()

print("Bai 2.2)")
toothpaste = df.get('toothpaste')
fig = plt.figure(figsize=(10, 7))
plt.scatter(month, toothpaste)
plt.title("Tooth Paste sales data")
plt.xlabel("Month Number")
plt.ylabel("Number of units Sold")
plt.show()

print("Bai 2.3)")
month = df.get('month_number')
facecream = df.get('facecream')
facewash = df.get('facewash')
plt.figure(figsize=(15, 7))
plt.bar(month+0.00, facecream, width=0.25)
plt.bar(month+0.25, facewash, width=0.25)
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(labels=['Face Cream sales', 'Face Wash sales'])
plt.xticks(month)
plt.title('Facewash and facecream sales data')
plt.show()

print("Bai 3)")

text = "No preprocessing, such as  cropping cropping cropping cropping or preprocessing, such as"
text = text.lower()
text = re.split("[^a-zA-Z0-9]", text)


data = collections.Counter(text)
data_words, data_freq = [], []
for k, v in data.most_common(30):
    data_words.append(k)
    data_freq.append(v)

plt.figure(figsize=(20, 10))
plt.plot(data_words, data_freq)
plt.xlabel('Word')
plt.ylabel('Frequency')
plt.title("Top 30 common words")
plt.show()
