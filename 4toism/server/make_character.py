from flask import Flask, request, jsonify
import gpt_api

# Flask 애플리케이션 생성
app = Flask(__name__)

# POST 요청을 처리하는 핸들러
@app.route('/characters/makeprompt', methods=['POST', 'GET'])
def make_character_prompt():
    #Spring으로부터 JSON 객체를 전달받음
    data = request.get_json()
    # data = {
    #     "sex" : "여자",
    #     "age" : "20-30대",
    #     "hairColor" : "갈색",
    #     "hairLength" : "단발",
    #     "skinColor" : "황인",
    #     "etc" : "안경을 썼다."
    # }
    
    # JSON 데이터에서 필요한 정보 추출
    prompt = f"{data['hairColor']}의 {data['hairLength']} 머리 스타일을 가진 {data['age']} {data['sex']} 캐릭터를 귀여운 웹툰 스타일로 그려주세요. 이 캐릭터는 {data['skinColor']} 피부를 가지고 있으며 {data['etc']}"

    # prompt = gpt_api.generate_gpt_prompt(input_data)

    # JSON 형식으로 추론 결과 반환
    return prompt

# Flask 애플리케이션 실행 - 0.0.0.0 으로 모든 IP에 대한 연결을 허용해놓고 포트는 8888로 설정
if __name__ == '__main__':
    app.run('0.0.0.0', port=8888, debug=True)