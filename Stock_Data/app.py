from user import User
from database import Database
import csv
import os

Database.initialise(database="stock_data",user="postgres",password="postgres1234", host="localhost")

for subfile in os.walk("C:\\Users\\rstoltzm\\Desktop\\Coding\\_Projects\\Stock_Analysis\\ETFs\\"):
    file_list = subfile[2]
    for file in file_list:
        print(file)
        with open(os.path.join("C:\\Users\\rstoltzm\\Desktop\\Coding\\_Projects\\Stock_Analysis\\ETFs\\",file)) as csvfile:
            text_file = csv.reader(csvfile)
            next(text_file, None)
            for row in text_file:
                user = User(file,row[0],row[1],row[2],row[3],row[4],row[5],row[6])
                user.save_to_db()
