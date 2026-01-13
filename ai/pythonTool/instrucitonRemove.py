import json
import os

# 原始檔案
input_file = "D:/VScode_repo/JsonEditFile_for_AIVtuber/Train.json"
# 去掉 instruction 後的檔案
output_file = "taiwanize_no_instruction.json"

# 讀取原始 JSON
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# 去掉 instruction
new_data = []
for item in data:
    new_item = {
        "input": item.get("input", ""),
        "output": item.get("output", "")
    }
    new_data.append(new_item)

# 存檔
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(new_data, f, ensure_ascii=False, indent=2)

print(f"✅ 已成功去掉 instruction，存成 {output_file}")