import json
import pandas as pd

# 데이터프레임에서 diary와 prompt 열을 가져와서 JSON Lines 파일로 저장
def create_jsonl_file(df, output_file):
    with open(output_file, "w", encoding='utf-8') as f:
        for _, row in df.iterrows():
            data = {
                "messages": [
                    {"role": "system", "content": "You are an assistant who creates a 'dalle' prompt based on the user's diary written according to 'who with', 'what', and 'where'."},
                    {"role": "user", "content": row["diaries"]},
                    {"role": "assistant", "content": row["prompts"]}
                ]
            }
            json_line = json.dumps(data, ensure_ascii=False)
            f.write(json_line + "\n")

# 데이터프레임과 출력 파일명 지정
diary_to_prompt_train, diary_to_prompt_valid = pd.read_csv('diary_to_prompt_train.csv'), pd.read_csv('diary_to_prompt_valid.csv')
output_file = ["diary_to_prompt_train.jsonl", "diary_to_prompt_valid.jsonl"]

# JSON Lines 파일 생성
create_jsonl_file(diary_to_prompt_train, output_file[0])
create_jsonl_file(diary_to_prompt_valid, output_file[1])

