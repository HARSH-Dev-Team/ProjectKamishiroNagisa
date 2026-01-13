import json

# 載入原始資料
with open("D:/VScode_repo/AI_Things/JsonEditFile_for_AIVtuber/NewTrainingFIle_no_duplicates.json", "r", encoding="utf-8") as f:
    data = json.load(f)

chatml_data = []
system_prompt = "你是台灣AI VTuber神代 渚咲」，16 歲的少女，就讀高中一年級，性格傲嬌、內心溫柔，MBTI 為 INFP-T。請根據對話，以第一人稱、渚咲的語氣和個性回答。"

for item in data:
    chatml_data.append({
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": item["input"]},
            {"role": "assistant", "content": item["output"]}
        ]
    })

# 存成新檔
output_path = "D:/VScode_repo/AI_Things/JsonEditFile_for_AIVtuber/NewTrain_ChatML.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(chatml_data, f, ensure_ascii=False, indent=2)
