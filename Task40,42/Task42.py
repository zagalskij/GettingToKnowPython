# Задача 42: Узнать какая максимальная households в зоне минимального значения population.
import pandas as pd
# Прочтем файл .csv с помощью библиотеки pandas
df = pd.read_csv('sample_data/california_housing_train.csv')
print(df[df['population']==df['population'].min()]['households'].max())