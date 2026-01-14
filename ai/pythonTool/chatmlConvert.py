import json

# 載入原始資料
with open("D:/ProjectKamishiroNagisa/ai/data/testTrainingFile.json", "r", encoding="utf-8") as f:
    data = json.load(f)

chatml_data = []
system_prompt = "你是台灣 AI VTuber \"神代 渚咲\" ，一位帥氣、自信、直率、自來熟、不受世俗框架束縛的少女。"

for item in data:
    chatml_data.append({
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": item["input"]},
            {"role": "assistant", "content": item["output"]}
        ]
    })

# 存成新檔
output_path = "D:/ProjectKamishiroNagisa/ai/data/testTrainingFile_chatml.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(chatml_data, f, ensure_ascii=False, indent=2)
