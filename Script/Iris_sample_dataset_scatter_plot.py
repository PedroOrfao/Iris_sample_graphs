import matplotlib.pyplot as plt
import pandas as pd

#Sample CSV from UCI Machine Learn Repository
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

#Since it lacks a header row, i am gonna add them manually
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = pd.read_csv(url, header=None, names=column_names)

#Separating de Dataset based on the iris type
set = df[df['class'] == 'Iris-setosa']
ver = df[df['class'] == 'Iris-versicolor']
vir = df[df['class'] == 'Iris-virginica']

#Scatter plot
plt.figure(figsize=(10,6))
plt.scatter(set['petal_length'], set['petal_width'], color='purple', label='Iris-setosa')
plt.scatter(ver['petal_length'], ver['petal_width'], color='blue', label='Iris-versicolor')
plt.scatter(vir['petal_length'], vir['petal_width'], color='yellow', label='Iris-virginica')

#labels
plt.xlabel('Petal Length (inch)')
plt.ylabel('Petal Width (inch)')
plt.title('Scatter plot of Sepal Length and Sepal Width with different types os Iris')
plt.legend()

#adding grid to the plot
plt.grid(True)

#Seeing plot
plt.show()
