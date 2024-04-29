import json
import os

file_path = "C:/Users/a4510/OneDrive/문서/kcc/dataset.json"

with open(file_path, 'r', encoding="utf-8") as dataset_json:
    dataset = json.load(dataset_json)

dev_data = dataset["dev"] 
train_data = dataset["train"]
print(len(dev_data), len(train_data))

with open("dev_dataset.json", 'w', encoding="utf-8") as dev_file:
    json.dump(dev_data, dev_file, indent=4, sort_keys=True, ensure_ascii=False)

with open("train_dataset.json", 'w', encoding="utf-8") as train_file:
    json.dump(train_data, train_file, indent=4, sort_keys=True, ensure_ascii=False)
