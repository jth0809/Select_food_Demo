import requests
import openai
from bs4 import BeautifulSoup
import pymysql

# DB 연결 설정
db_host = "localhost"
db_user = "sf-user"
db_password = "A4q8EEdh3c"
openai.api_key = "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"
# DB 연결
connect = pymysql.connect(host=db_host, user=db_user, password=db_password,db='SelectFood',charset='utf8')
cur = connect.cursor()

def get_user_location():
    latitude = input("현재 위도를 입력하세요: ")
    longitude = input("현재 경도를 입력하세요: ")
    return latitude, longitude

# 현재 위치를 기반으로 주변 음식점 정보를 가져오는 함수
def get_nearby_restaurants(latitude, longitude):
    sql = "SELECT 사업장명, latitude, longitude FROM restaurant LIMIT 10;"
    cur.execute(sql)
    nearby_restaurants = [{'사업장명': row[0], 'latitude': row[1], 'longitude': row[2]} for row in cur.fetchall()]
    return nearby_restaurants 

# 네이버 API 설정
URL = "https://openapi.naver.com/v1/search/local.json"
NAVERAPIKEY = {
    "X-Naver-Client-Id": "rUgonfL9PeB980TGm6Lr",
    "X-Naver-Client-Secret": "1m9f9uPZ1i"
}

# 메뉴 크롤링
def crawl_menu(data):
    if data:
        url = "https://map.naver.com/v5/search/" + data
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        try:
            entry_frame = soup.find('entryiframe', {'id': 'entryiframe'})
            if entry_frame:
                entry_url = entry_frame['src']
                entry_response = requests.get(entry_url)
                entry_response.raise_for_status()

                entry_soup = BeautifulSoup(entry_response.content, 'html.parser')
                menu_element = entry_soup.find('div', {'class': '_3ak_I'})
                if menu_element:
                    return menu_element.text
                else:
                    return "메뉴가 없습니다"
            else:
                return "메뉴 정보를 찾을 수 없습니다"
        except Exception as e:
            return str(e)
    else:
        return "유효한 URL이 없습니다."


# 가게 정보 가져오기
def get_store_info(query):
    params = {
        'query': query,
        'display': 1,  # 검색 결과 출력 건수 (최대 100)
        'start': 1,   # 검색 시작 위치
        'sort': 'sim'  # 정렬 옵션: 유사도순
    }
    headers = NAVERAPIKEY
    response = requests.get(URL, params=params, headers=headers)

    if response.status_code != 200:
        return None
    store_info= response.json()
    if store_info and 'items' in store_info and store_info['items']:
        return store_info['items'][0]
    else:
        return None

# 네이버 검색을 통해 음식점 메뉴 정보 가져오기
def search_and_get_menu(query):
    store_data = get_store_info(query)

    if store_data:
        title = store_data.get('title')
        link = store_data.get('link')
        
        menu_info = crawl_menu(link)
        return {'사업장명': title, 'menu_info': menu_info}

    return None

latitude, longitude = get_user_location()
# 현재 위치를 기반으로 주변 음식점 정보 가져오기
nearby_restaurants = get_nearby_restaurants(latitude, longitude)

# 가게명과 메뉴이름만 출력
for restaurant in nearby_restaurants:
    result = search_and_get_menu(restaurant['사업장명'])
    if result:
        print(f"가게명: {result['사업장명']}")
        print(f"메뉴 정보:\n{result['menu_info']}")
        print()
    else:
        print(f"{restaurant['사업장명']}의 정보를 가져올 수 없습니다.")
async def recommend_food():
    request_data = request.get_json()
    user_disease = request_data.get('user_disease')
    user_allergy = request_data.get('user_allergy')
    user_vegan = request_data.get('user_vegan')
    food_name = request_data.get('food_name')


input("음식:",food_name)
completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You will be presented with food names and your job is to provide a set of tags. Provide your answer in bullet point form.\nAnd if specific person can't eat provided food, tell me who can't eat due to allergy or disease\nDepending on whether the user is vegan or not, please determine whether he can eat or not and print it out as a tag, If I give you the food menus, you should arrange the food in order of preference:"
            },
            {
                "role": "user",
                "content": f"food:{food_name}\nDisease: {user_disease}\nAllergy: {user_allergy}\nVegan: {user_vegan}"
            }
        ],
        temperature=0,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
recommended_foods.append(completion.choices[0].message.content)  # OpenAI에서 받은 음식을 추가

response_data = {
        'recommended_foods': recommended_foods,
        'unavailable_foods': unavailable_foods,
        'error': None
}

    # 음식 정보 출력
print("음식 정보:", food_info)
    # OpenAI 응답 출력
print("OpenAI 응답:", recommended_foods)

# DB 연결 종료
connect.close()
