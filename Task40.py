# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data. 
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).
import pandas as pd
# Прочтем файл .csv с помощью библиотеки pandas
df = pd.read_csv('/home/zagalskij/GIT/GettingToKnowPython/lesson9/sample_data/california_housing_train.csv')
