#!/usr/bin/env python
# coding: utf-8

# # Import necessary libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # Data Processing

# ### Load the dataset into a pandas DataFrame

# In[2]:


file_path = 'GlobalWeatherRepository.csv'  
df = pd.read_csv(file_path)


# ### Display the first few rows

# In[3]:


print("First few rows of the dataset:")
print(df.head())


# ### Display Dataset Information

# In[4]:


print(df.info())


# ### Missing Value Checking

# In[5]:


print("\nMissing values in each column:")
print(df.isnull().sum())


# ### Convert columns to appropriate data types

# In[6]:


df['temperature_celsius'] = pd.to_numeric(df['temperature_celsius'], errors='coerce')
df['humidity'] = pd.to_numeric(df['humidity'], errors='coerce')


# ### Save the cleaned dataset 

# In[7]:


df.to_csv('Cleaned_GlobalWeather.csv', index=False)


# ### Display a summary of key statistics

# In[8]:


print("\nSummary statistics for key weather attributes:")
print(df[['temperature_celsius', 'humidity', 'precip_mm', 'wind_mph']].describe())


# # Data Analytics and Visualization

# ## 1. Generate a summary of the top 5 hottest and coldest locations globally 

# In[9]:


top_5_hottest = df.nlargest(5, 'temperature_celsius')[['location_name', 'temperature_celsius']]
top_5_coldest = df.nsmallest(5, 'temperature_celsius')[['location_name', 'temperature_celsius']]


# In[10]:


print("\nTop 5 hottest locations globally:")
print(top_5_hottest)


# In[11]:


print("\nTop 5 coldest locations globally:")
print(top_5_coldest)


# In[12]:


top_5_air_pollution = df.nlargest(5, 'air_quality_Carbon_Monoxide')[['location_name', 'air_quality_Carbon_Monoxide']]
print("\nTop 5 locations with highest Carbon Monoxide levels:")
print(top_5_air_pollution)


# ## 2. Group the data by country and compute average temperature, precipitation, and humidity

# In[13]:


grouped_data = df.groupby('country').agg({
    'temperature_celsius': ['mean', 'max', 'min'],
    'precip_mm': 'sum',
    'humidity': 'mean'
}).reset_index()


# In[14]:


print("\nGrouped data by country (average temperature, precipitation, and humidity):")
print(grouped_data)


# ## 3. Plot Visualizations

# ### a. Histogram of temperatures

# In[15]:


plt.figure(figsize=(10,6))
sns.histplot(df['temperature_celsius'], bins=30, color='blue', kde=True)
plt.title('Histogram of Global Temperatures')
plt.xlabel('Temperature (Celsius)')
plt.ylabel('Frequency')
plt.show()


# ### b. Line graph showing temperature changes over time for Kabul Region

# In[16]:


kabul_data = df[df['location_name'] == 'Kabul']

plt.figure(figsize=(10,6))
plt.plot(kabul_data['last_updated'], kabul_data['temperature_celsius'], marker='o')
plt.title('Temperature Changes Over Time in Kabul')
plt.xlabel('Time')
plt.ylabel('Temperature (Celsius)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


# ### Average air quality by country (for Carbon Monoxide levels)

# In[17]:


air_quality_by_country = df.groupby('country')['air_quality_Carbon_Monoxide'].mean().sort_values(ascending=False)

plt.figure(figsize=(12,8))
air_quality_by_country.plot(kind='bar', color='red')
plt.title('Average Carbon Monoxide Levels by Country')
plt.ylabel('Carbon Monoxide (µg/m³)')
plt.show()


# ### Group data by moon phase and calculate the average temperature for each phase

# In[18]:


moon_phase_analysis = df.groupby('moon_phase')['temperature_celsius'].mean()

plt.figure(figsize=(10,6))
moon_phase_analysis.plot(kind='bar', color='purple')
plt.title('Average Temperature by Moon Phase')
plt.ylabel('Temperature (Celsius)')
plt.show()


# In[ ]:




