import openai
import requests
import json
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

app.config['JSON_AS_ASCII']=False

# OpenAI API 설정
openai.api_key = "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"

async def get_food_info(food_name):
    return True
#async def get_foods_list(disease, allergy, vegan):
    # 사용자의 질병, 알레르기, 비건 여부에 따라 음식 리스트 반환 코드
    # 예를 들어, 비건이면 비건 식단을, 알레르기가 있다면 알레르기에 주의해야 하는 식단을 추천할 수 있습니다.
@app.route('/ai/recommend_food', methods=['POST'])
async def recommend_food():
    request_data = request.get_json()
    user_disease = request_data.get('user_disease')
    user_allergy = request_data.get('user_allergy')
    user_vegan = request_data.get('user_vegan')
    food_name = request_data.get('food_name')

    
    print(food_name)
    food_info = get_food_info(food_name)

    if food_info is None:
        response_data = {
            'recommended_foods': [],
            'unavailable_foods': [],
            'error': '음식 정보를 가져오지 못했습니다.'
        }
        return jsonify(response_data)

    print("Going to ask gpt")

    recommended_foods = []  # 추천 가능한 음식 리스트
    unavailable_foods = []  # 먹을 수 없는 음식 리스트

    # OpenAI API 호출을 통해 음식 추천
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": " Provide your answer in bullet point form And if specific person can't eat provided food, tell me who can't eat due to allergy or disease Depending on whether the user is vegan or not, please determine whether he can eat or not and print it out as a tag, If I give you the food menus, you should arrange the food in order of preference:"
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
        'recommended_foods': recommended_foods#,
        #'unavailable_foods': unavailable_foods,                   
        #'error': None
    }

    # 음식 정보 출력
    print("음식 정보:", food_info)
    # OpenAI 응답 출력s
    print("OpenAI 응답:", recommended_foods)

    result = json.dumps(response_data, ensure_ascii=False)
    res = make_response(result)
    return res

if __name__ == '__main__':
    app.run(debug=True)
