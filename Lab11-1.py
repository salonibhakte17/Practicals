import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

plt.plot(df['Month'], df['TotalProfit'], marker='o')
plt.title("Total Profit Per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.grid()
plt.show()

plt.plot(df['Month'], df['FaceCream'], label='Face Cream')
plt.plot(df['Month'], df['FaceWash'], label='Face Wash')
plt.plot(df['Month'], df['Toothpaste'], label='Toothpaste')
plt.plot(df['Month'], df['BathingSoap'], label='Soap')
plt.legend()
plt.title("Product Sales Data")
plt.show()

x = range(len(df['Month']))
plt.bar(x, df['FaceCream'], width=0.4, label='Face Cream')
plt.bar([i+0.4 for i in x], df['FaceWash'], width=0.4, label='Face Wash')
plt.xticks([i+0.2 for i in x], df['Month'])
plt.legend()
plt.title("Face Cream vs Face Wash Sales")
plt.show()

total_sales = [
    df['FaceCream'].sum(),
    df['FaceWash'].sum(),
    df['Toothpaste'].sum(),
    df['BathingSoap'].sum(),
    df['Shampoo'].sum(),
    df['Moisturizer'].sum()
]

labels = ['FaceCream','FaceWash','Toothpaste','Soap','Shampoo','Moisturizer']

plt.pie(total_sales, labels=labels, autopct='%1.1f%%')
plt.title("Yearly Sales Distribution")
plt.show()