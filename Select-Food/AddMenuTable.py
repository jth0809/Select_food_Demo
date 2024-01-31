from pyproj import Proj, transform
import pandas as pd
import numpy as np
import pymysql
import requests
import asyncio
import json
import threading
import multiprocessing
from functools import partial

# DB 연결 설정
DB_HOST = "localhost"
DB_USER = "sf-user"
DB_PW = "A4q8EEdh3c"

def getMenu(length: int, data: list):
    connect = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PW, charset='utf8')
    cur = connect.cursor()
    cur.execute("USE SelectFood")

    ID = data[0]
    Name = data[1]

    cur.execute("Select id From menu where id = '{0}';".format(ID))
    preExistID = cur.fetchall()

    if len(preExistID) > 0:
        if ID == preExistID[0][0]:
            print("Skipping '{0}', name:{1}".format(ID, Name) + "( " + str(data[2]/length) + "% )")
            return

    Result = list()
    uri = "https://www.happytanuki.kr/GetMenusByName?Name=" + Name
    responseData = requests.get(uri)

    if responseData.ok != True:
        return

    Result = responseData.json()["Menus"]

    for item in Result:
        SQL = "Insert ignore Into menu (id, menu) values (%s, %s);"
        cur.execute(SQL, (ID, item))
        print("\033[33m" + Name + ':' + ID + " " + item + "\033[0m" + "( " + str(data[2]/length) + "% )")
    connect.commit()

    cur.close()
    connect.close()

    #print("\033[33m" + Name + "\033[0m" + " " + json.dumps(requests.get(uri).json(), ensure_ascii=False))

def listStrip(myList: list):
    ReturnValue = list()

    for item in myList:
        ReturnValue.append([item[0], item[1], item[3]])
    
    return ReturnValue

def main():
    asyncobject = list()

    print("\033[33m" + "Getting Names.." + "\033[0m")

    connect = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PW, charset='utf8')
    cur = connect.cursor()

    cur.execute("USE SelectFood")
    cur.execute("Select id, name, \
                (6371 * ACos(Cos(Radians(latitude)) * Cos(Radians(37.2092017)) * Cos(Radians(126.9769365) - Radians(longitude)) + Sin(Radians(latitude)) * Sin(Radians(37.2092017)))) as Distance, \
                    row_number() over(order by id) as num \
                    From restaurant \
                    Having Distance <= 20 \
                    Order By Distance ASC;")

    RESTAURANTS = cur.fetchall()

    cur.close()
    connect.close()

    print("\033[33m" + "Complete." + "\033[0m")
    print("\033[33m" + "Process pool executing.." + "\033[0m")

    processPool = multiprocessing.Pool(5)
    processPool.map(partial(getMenu, len(RESTAURANTS)), listStrip(RESTAURANTS))
    processPool.close()
    processPool.join()

if __name__ == "__main__":
    main()