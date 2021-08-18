# This is a sample Python script.
import pandas as pd
import pymysql


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def open_excel():
    # Use a breakpoint in the code line below to debug your script.
    df = pd.read_excel(r'E:\MIT Unimelb\2021 second semester\Hackiethon Recipe 2021\Recipe.xlsx')
    for i in range(0, df['食谱ID'].size):
        sql = 'INSERT INTO recipes (rec_id, name, calorie, ingredient_list, type, description, likes, create_time) ' \
              'VALUES (\''
        sql = sql + str(df.iloc[i, 0]) + '\', \'' + str(df.iloc[i, 1]) + '\', \'' + str(df.iloc[i, 2]) + '\', \'' \
              + str(df.iloc[i, 3]) + '\', \'' + str(df.iloc[i, 4]) + '\', \'' + str(df.iloc[i, 5]) + '\', 0, now())'
        print(sql)
        cursor.execute(sql)
    # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    db = pymysql.connect(host='localhost', user='root', password='root1998', database='recipeweb')
    cursor = db.cursor()
    open_excel()
    db.commit()
    db.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
