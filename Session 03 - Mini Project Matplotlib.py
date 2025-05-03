#!/usr/bin/env python
# coding: utf-8

# <div class="alert alert-block alert-success">
#     <h1 align="center">Machine Learning in Python</h1>
#     <h3 align="center">Mini Project1</h3>
# </div>

# <img src = "https://www.cyclonis.com/images/2020/03/googleplay.jpg" width=50%>

# ## Importing the libraries

# In[29]:


import numpy as np
import pandas as pd


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import seaborn as sns


# ## Load and Prepare Data

# In[30]:


df = pd.read_csv("googleplaystore.csv")
df.head()


# In[ ]:





# ## EDA

# In[31]:


df.tail()


# In[32]:


df.shape


# In[33]:


df.info()


# In[34]:


df.describe()


# In[35]:


type(df.head)


# In[36]:


df.columns


# In[37]:


df.dtypes


# ## Data Preprocessing
# 

# In[38]:


df.isnull().sum()


# In[39]:


plt.figure(figsize=(8, 6))
sns.boxplot(df['Rating'])
plt.title("Boxplot of Rating")
plt.show()


# In[40]:


print (df[df['Rating'] == 19])


# In[41]:


df = df.drop(10472, errors='ignore')


# In[42]:


df = df[df['Rating'] <= 5]


# In[43]:


df['Rating_NaN'] = df["Rating"].isnull().astype(int)


# In[44]:


median_rating = df['Rating'].median()
df['Rating'] = df['Rating'].fillna(median_rating)


# In[45]:


df.isnull().sum()


# In[46]:


mode_current_ver = df['Current Ver'].mode()[0]
df['Current Ver'] = df['Current Ver'].fillna(mode_current_ver)

mode_android_ver = df['Android Ver'].mode()[0]
df['Android Ver'] = df['Android Ver'].fillna(mode_android_ver)


# In[47]:


df.isnull().sum()


# ## Strorytelling - Visualization
# 

# In[48]:


#بررسی توزیع و فراوانی مقادیر Rating
plt.figure(figsize=(10, 6))
sns.histplot(df['Rating'], bins=20, kde=True)
plt.title("Distribution of Rating")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.show()


# In[49]:


#بررسی توزیع و وجود مقادیر پرت (outliers) در رتبه بندی اپلیکیشن ها.
plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='Rating', data=df)
plt.xlabel("Category")
plt.ylabel("Rating")
plt.show()


# In[50]:


# مقایسه تعداد نصب ها بین دسته بندی های مختلف
df['Installs'] = df['Installs'].str.replace("+", "").str.replace(',', '').astype(int)

plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Installs', data=df, ci=None)
plt.xticks(rotation=90)
plt.title('Total Installs by Category')
plt.xlabel('Category')
plt.ylabel("Total Installs")
plt.show()


# In[51]:


#تحلیل ارتباط بین تعداد نصب ها و رتبه بندی
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Installs', y='Rating', data=df, alpha=0.5)
plt.xscale('log')
plt.title("Relationship Between Installs and Ratings")
plt.xlabel("Installs (log scale)")
plt.ylabel('Rating')
plt.show()


# In[52]:


#شمارش تعداد اپلیکیشن ها بر اساس نوع (Type)
plt.figure(figsize=(5, 4))
sns.countplot(x='Type' , data=df)
plt.title("Count of Apps by Type")
plt.xlabel("Type")
plt.ylabel("Conut")
plt.show()


# In[53]:


#بررسی همبستگی بین ویژگی های عددی
plt.figure(figsize=(10, 8))
correlation = df.corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()


# ## Send us the Result (Maktabkhoone)

# In[55]:


import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save the model to a file
filename = 'finalized_model.pkl'
pickle.dump(model, open(filename, 'wb'))


# In[ ]:




