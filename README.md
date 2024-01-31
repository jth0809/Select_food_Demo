# Select_food_Demo

2023.09 ~ 2023.11(2개월)

메뉴 추천 서비스의 데모 버전

FE: 리액트

BE: 스프링 부트

AI: 플라스크 / chatGPT 4.0

# 프로젝트 계획

각각의 요소가 서로 웹 소켓을 이용해 통신하며 외부 API로 요청을 보내어 필요한 정보를 가져옵니다.

공공 API와 네이버 지도를 이용해서 이용자 주변의 식당명과 메뉴를 가져오고 AI를 이용해 태그를 붙입니다.

이용자가 설정한 질병, 알레르기, 종교, 영양 정보 등의 고려 사항을 태그와 함께 AI로 판단해서 표시 여부를 결정하고

공공 API의 식품 영양 정보 데이터의 메뉴와 유사한 메뉴인지 판단하여 영양 정보와 같은 자세한 식품의 정보를 출력합니다.

# 프로젝트 문제

`네이버 지도를 통해 얻은 메뉴의 이름과 공공 API에서 얻은 메뉴의 이름의 연관성을 찾는 문제`

`메뉴에 태그를 붙일 때 태그의 후보 이름과의 연관성을 찾는 문제`

# 프로젝트 경과

본 프로젝트는 대학교 2학년 프로젝트 수업에서 제작되었습니다.

각 요소의 연결과 통신은 빠르게 구현되었으나 이름 간 연관성을 찾는 문제에 시간이 지연되었습니다.

때문에 직접 일부 데이터를 삽입하여 이용자의 설정에 따른 메뉴를 추천하고 클릭 시 정보를 출력하는 DEMO 버전이 되었습니다.

# 프로젝트 회고

급하게 코드를 작성했고 프레임워크를 처음 다루다 보니 가독성, 최적화, 테스트 등을 신경 쓰지 못한 점이 아쉽습니다.

이번 기회를 계기로 더욱 발전하고 성장하기 위해 노력할 것입니다.
