from extract import scrape_sunglasses
from transform import clean_data
from load import database_load
import datetime

dataframe = scrape_sunglasses()
data = clean_data(dataframe)
database_load(data)

file = open(r'C:\Users\zayed\PycharmProjects\webscrapping_sunglasshut\task.txt', 'a')
file.write(f'{datetime.datetime.now()} - The script ran \n')
file.close()
