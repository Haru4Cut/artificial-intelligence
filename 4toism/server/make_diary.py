from flask import Flask, request, jsonify
import call_gpt_api
from call_gpt_api import haruFour

# Flask 애플리케이션 생성
app = Flask(__name__)

# POST 요청을 처리하는 핸들러
@app.route('/events/makeprompt', methods=['POST', 'GET'])
def make_diary_prompt():
    #Spring으로부터 JSON 객체를 전달받음
    data = request.get_json()
    # data = [
    #     {
    #         "cutNum" : 2,
    #         "emotion" : '기쁨',
    #         "keywords" : ["아빠랑", "카페에서","커피를 마셨다"],
    #         "date" : "2022-08-11",
    #         "orderNum" : 0
    #     },
    #     {
    #         "cutNum" : 2,
    #         "emotion" : 2,
    #         "keywords" : ["아빠랑", "카페에서","커피를 마셨다"],
    #         "date" : "2022-08-11",
    #         "orderNum" : 1
    #     }
    #  ]

    # JSON 데이터에서 필요한 정보 추출
    cut_num = len(data)
    diary_prompt = {}
    if cut_num == 1:
        diary = data[0]

        # 일기 키워드와 감정 키워드 추출
        input_data = diary['keywords']
        input_data.append(diary['emotion'])

        # AI 모델을 호출하여 입력 데이터에 대한 프롬프트 생성
        prompt = haruFour().gpt_api(input_data)
        diary_prompt[diary['orderNum']] = prompt + "+ you can see it vertically"
    else:
        for diary in data:
            # 일기 키워드와 감정 키워드 추출
            input_data = diary['keywords']
            input_data.append(diary['emotion'])
            
            # AI 모델을 호출하여 입력 데이터에 대한 프롬프트 생성
            diary_prompt[diary['orderNum']] = haruFour().gpt_api(input_data)

    return diary_prompt

# Flask 애플리케이션 실행 - 0.0.0.0 으로 모든 IP에 대한 연결을 허용해놓고 포트는 8082로 설정
if __name__ == '__main__':
    # make_diary_prompt()
    app.run('0.0.0.0', port=8082, debug=True)

    