import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"/Users/sabarish/Downloads/brain_tumor_dataset.csv")

data.head()

data.isnull().sum()

data.duplicated().sum()

data.describe()

data.info()

plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Tumor Type', palette='viridis')
plt.title('Distribution of Tumor Types')
plt.xlabel('Tumor Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='Size (cm)', y='Patient Age', hue='Tumor Type', palette='viridis', alpha=0.7)
plt.title('Tumor Size vs. Patient Age')
plt.xlabel('Size (cm)')
plt.ylabel('Patient Age')
plt.grid(True)
plt.show()

sns.pairplot(data, vars=['Size (cm)', 'Patient Age'], hue='Tumor Type', palette='viridis')
plt.suptitle('Pairplot of Size and Age by Tumor Type', y=1.02)
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x='Gender', y='Size (cm)', palette='viridis')
plt.title('Tumor Size by Gender')
plt.xlabel('Gender')
plt.ylabel('Size (cm)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='Patient Age', hue='Gender', multiple='stack', palette='viridis')
plt.title('Age Distribution by Gender')
plt.xlabel('Patient Age')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

