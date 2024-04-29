import json
import os
import kotka

from kotka.lipogram import replace_phoneme
from kotka.lipogram.rules import SquareDog
from kotka.yaminizer import encode_yamin
from kotka.shredder import shred_syllable

#current_path = os.getcwd()
#print(current_path)

nli = os.listdir("C:/Users/a4510/OneDrive/문서/kcc/klue-nli-v1")
sts = os.listdir("C:/Users/a4510/OneDrive/문서/kcc/klue-sts-v1")

#dev data
dev_data = []

file_name = nli[0]
file_path = "C:/Users/a4510/OneDrive/문서/kcc/klue-nli-v1"+'/'+file_name

with open(file_path, 'r', encoding="utf-8") as json_file:
    nli_dev_data = json.load(json_file)

    
for i in range(0, len(nli_dev_data)):
    if nli_dev_data[i]['source'] == "airbnb":
        if i == 0:
            original_data = nli_dev_data[i]['premise']
            obfuscation1 = replace_phoneme(original_data, rule=SquareDog())
            obfuscation2 = encode_yamin(original_data)
            obfuscation3 = shred_syllable(original_data, active_rate=0.5)
            dev_data.append({"original_data" : original_data, "obfuscation1" : obfuscation1, "obfuscation2" : obfuscation2, "obfuscation3" : obfuscation3})
        elif nli_dev_data[i]['premise'] == nli_dev_data[i-1]['premise']:
            continue
        else:
            original_data = nli_dev_data[i]['premise']
            obfuscation1 = replace_phoneme(original_data, rule=SquareDog())
            obfuscation2 = encode_yamin(original_data)
            obfuscation3 = shred_syllable(original_data, active_rate=0.5)
            dev_data.append({"original_data" : original_data, "obfuscation1" : obfuscation1, "obfuscation2" : obfuscation2, "obfuscation3" : obfuscation3})
            


file_name = sts[0]
file_path = "C:/Users/a4510/OneDrive/문서/kcc/klue-sts-v1"+'/'+file_name

with open(file_path, 'r', encoding="utf-8") as json_file:
    sts_dev_data = json.load(json_file)


for i in range(0, len(sts_dev_data)):
    if sts_dev_data[i]["source"] == "airbnb-rtt":
        if i == 0:
            original_data = sts_dev_data[i]['sentence1']
            obfuscation1 = replace_phoneme(original_data, rule=SquareDog())
            obfuscation2 = encode_yamin(original_data)
            obfuscation3 = shred_syllable(original_data, active_rate=0.5)
            dev_data.append({"original_data" : original_data, "obfuscation1" : obfuscation1, "obfuscation2" : obfuscation2, "obfuscation3" : obfuscation3})
        elif sts_dev_data[i]['sentence1'] == sts_dev_data[i-1]['sentence1']:
            continue
        else:
            original_data = sts_dev_data[i]['sentence1']
            obfuscation1 = replace_phoneme(original_data, rule=SquareDog())
            obfuscation2 = encode_yamin(original_data)
            obfuscation3 = shred_syllable(original_data, active_rate=0.5)
            dev_data.append({"original_data" : original_data, "obfuscation1" : obfuscation1, "obfuscation2" : obfuscation2, "obfuscation3" : obfuscation3})
            
    elif sts_dev_data[i]['sentence1'] == "airbnb-sampled":
        if i == 0:
            original_data = sts_dev_data[i]['sentence1']
            obfuscation1 = replace_phoneme(original_data, rule=SquareDog())
            obfuscation2 = encode_yamin(original_data)
            obfuscation3 = shred_syllable(original_data, active_rate=0.5)
            dev_data.append({"original_data" : original_data, "obfuscation1" : obfuscation1, "obfuscation2" : obfuscation2, "obfuscation3" : obfuscation3})
        elif sts_dev_data[i]['sentence1'] == sts_dev_data[i-1]['sentence1']:
            continue
        else:
            original_data = sts_dev_data[i]['sentence1']
            obfuscation1 = replace_phoneme(original_data, rule=SquareDog())
            obfuscation2 = encode_yamin(original_data)
            obfuscation3 = shred_syllable(original_data, active_rate=0.5)
            dev_data.append({"original_data" : original_data, "obfuscation1" : obfuscation1, "obfuscation2" : obfuscation2, "obfuscation3" : obfuscation3})

#train_data
train_data = []

file_name = nli[1]
file_path = "C:/Users/a4510/OneDrive/문서/kcc/klue-nli-v1"+'/'+file_name

with open(file_path, 'r', encoding="utf-8") as json_file:
    nli_train_data = json.load(json_file)


for i in range(0, len(nli_train_data)):
    if nli_train_data[i]["genre"] == "airbnb":
        if i == 0:
            original_data = nli_train_data[i]['premise']
            obfuscation1 = replace_phoneme(original_data, rule=SquareDog())
            obfuscation2 = encode_yamin(original_data)
            obfuscation3 = shred_syllable(original_data, active_rate=0.5)
            train_data.append({"original_data" : original_data, "obfuscation1" : obfuscation1, "obfuscation2" : obfuscation2, "obfuscation3" : obfuscation3})
        elif nli_train_data[i]['premise'] == nli_train_data[i-1]['premise']:
            continue
        else:
            original_data = nli_train_data[i]['premise']
            obfuscation1 = replace_phoneme(original_data, rule=SquareDog())
            obfuscation2 = encode_yamin(original_data)
            obfuscation3 = shred_syllable(original_data, active_rate=0.5)
            train_data.append({"original_data" : original_data, "obfuscation1" : obfuscation1, "obfuscation2" : obfuscation2, "obfuscation3" : obfuscation3})


file_name = sts[1]
file_path = "C:/Users/a4510/OneDrive/문서/kcc/klue-sts-v1"+'/'+file_name

with open(file_path, 'r', encoding="utf-8") as json_file:
    sts_train_data = json.load(json_file)


for i in range(0, len(sts_train_data)):
    if sts_train_data[i]["source"] == "airbnb-rtt":
        if i == 0:
            original_data = sts_train_data[i]['sentence1']
            obfuscation1 = replace_phoneme(original_data, rule=SquareDog())
            obfuscation2 = encode_yamin(original_data)
            obfuscation3 = shred_syllable(original_data, active_rate=0.5)
            train_data.append({"original_data" : original_data, "obfuscation1" : obfuscation1, "obfuscation2" : obfuscation2, "obfuscation3" : obfuscation3})
        elif sts_train_data[i]['sentence1'] == sts_train_data[i-1]['sentence1']:
            continue
        else:
            original_data = sts_train_data[i]['sentence1']
            obfuscation1 = replace_phoneme(original_data, rule=SquareDog())
            obfuscation2 = encode_yamin(original_data)
            obfuscation3 = shred_syllable(original_data, active_rate=0.5)
            train_data.append({"original_data" : original_data, "obfuscation1" : obfuscation1, "obfuscation2" : obfuscation2, "obfuscation3" : obfuscation3})
    elif sts_train_data[i]['sentence1'] == "airbnb-sampled":
        if i == 0:
            original_data = sts_train_data[i]['sentence1']
            obfuscation1 = replace_phoneme(original_data, rule=SquareDog())
            obfuscation2 = encode_yamin(original_data)
            obfuscation3 = shred_syllable(original_data, active_rate=0.5)
            train_data.append({"original_data" : original_data, "obfuscation1" : obfuscation1, "obfuscation2" : obfuscation2, "obfuscation3" : obfuscation3})
        elif sts_train_data[i]['sentence1'] == sts_train_data[i-1]['sentence1']:
            continue
        else:
            original_data = sts_train_data[i]['sentence1']
            obfuscation1 = replace_phoneme(original_data, rule=SquareDog())
            obfuscation2 = encode_yamin(original_data)
            obfuscation3 = shred_syllable(original_data, active_rate=0.5)
            train_data.append({"original_data" : original_data, "obfuscation1" : obfuscation1, "obfuscation2" : obfuscation2, "obfuscation3" : obfuscation3})

all_data = {"dev" : dev_data, "train" : train_data}

with open("dataset.json", 'w', encoding="utf-8") as all_file:
    json.dump(all_data, all_file, indent=4, sort_keys=True, ensure_ascii=False)


#with open("dataset.json", 'w', encoding="utf-8") as nli_data:
#    json.dump(data, nli_data, indent=4, sort_keys=True, ensure_ascii=False)





