
# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data. 
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).
# Библиотека для работы с табличными данными
import pandas as pd
# Прочтем файл .csv с помощью библиотеки pandas
df = pd.read_csv('sample_data/california_housing_train.csv')
print(df[(df['population'] < 501)&(df['population'] > 0)]['median_house_value'].mean())