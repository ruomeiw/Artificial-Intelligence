import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_excel('hw2.xlsx')
df[['Positive_sentiment', 'Negative_sentiment']
   ] = df['Sentiment'].str.split(' ', expand=True)
df[['Positive_sentiment', 'Negative_sentiment']] = df[[
    'Positive_sentiment', 'Negative_sentiment']].fillna(0)
df['Positive_sentiment'] = df['Positive_sentiment'].astype('int')
df['Negative_sentiment'] = df['Negative_sentiment'].astype('int')


# print(data.corr())

data = df.drop(['Tweet ID', 'Username', 'Timestamp', 'Entities',
               'Sentiment', 'Mentions', 'Hashtags', 'URLs'], axis=1)

print(data.corr(method='pearson'))
