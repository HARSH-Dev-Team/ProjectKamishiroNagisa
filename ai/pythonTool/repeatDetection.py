import json

# 讀取資料
# file_path = "D:\ProjectKamishiroNagisa\ai\data\" # 自己改位子
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"總樣本數: {len(data)}")

# 用 set 檢查重複，只保留第一個
seen = set()
unique_data = []
duplicates = []

for i, sample in enumerate(data):
    key = (sample["input"], sample["output"])
    if key in seen:
        duplicates.append((i, sample))
    else:
        seen.add(key)
        unique_data.append(sample)

if duplicates:
    print(f"⚠️ 發現 {len(duplicates)} 筆重複樣本（已刪除重複，只保留第一筆）：")
    for idx, dup in duplicates:
        print(f"- 索引 {idx}: input={dup['input']}, output={dup['output']}")
else:
    print("✅ 沒有發現重複樣本")

# 詢問使用者是否要儲存無重複的新 JSON 檔
save_choice = input("是否要儲存無重複的新檔案？(y/yes 以儲存): ").strip().lower()
if save_choice in ("y", "yes"):
    output_path = "D:/VScode_repo/AI_Things/JsonEditFile_for_AIVtuber/NewTrainingFIle_no_duplicates.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(unique_data, f, ensure_ascii=False, indent=2)
    print(f"已儲存無重複樣本至 {output_path}")
else:
    print("未儲存新檔案。")
