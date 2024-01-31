import pymysql

# DB 연결 설정
DB_HOST = "localhost"
DB_USER = "sf-user"
DB_PW = "A4q8EEdh3c"

def Tagging():
    connect = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PW, charset='utf8')
    cur = connect.cursor()
    cur.execute("USE SelectFood")

    cur.execute("select menu from menu;")

    data = cur.fetchall()
    stringToPrint = contert(data)

    with open("out.txt", "w") as out:
        out.write("다음 음식들을 포함된 원재료에 따라 분류해서 태그를 달아줘:\n")
        out.write(stringToPrint)

def contert(data):
    returnValue = str()

    while (data[0][0] == "This restaurant has no menu data" or data[0][0] == "No such restaurant"):
        data = data[1:]
    
    returnValue += data[0][0]
    for item in data[1:]:
        if (item[0] == "This restaurant has no menu data" or item[0] == "No such restaurant"):
            continue
        returnValue += ',' + item[0]

    return returnValue

Tagging()