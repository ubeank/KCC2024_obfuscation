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

# test set
file_path = "C:/Users/a4510/OneDrive/문서/kcc/dev_dataset.json"

with open(file_path, 'r', encoding="utf-8") as dev_dataset_json:
    dataset = json.load(dev_dataset_json)

for_dev_data = []
for_test_data = []
for i in range(0, len(dataset)):
    if(i < 154):
        for_dev_data.append(dataset[i])
    else:
        for_test_data.append(dataset[i])

print(len(for_dev_data), len(for_test_data))

with open("val_dataset.json", 'w', encoding="utf-8") as val_file:
    json.dump(for_dev_data, val_file, indent=4, sort_keys=True, ensure_ascii=False)

with open("test_dataset.json", 'w', encoding="utf-8") as test_file:
    json.dump(for_test_data, test_file, indent=4, sort_keys=True, ensure_ascii=False)
