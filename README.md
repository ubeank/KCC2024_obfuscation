# kcc
#하이퍼파라미터 서칭

#learing_rate = 2e-05 / epoch = 3.0
```
python run_summarization.py \
    --model_name_or_path KETI-AIR/ke-t5-small-ko \
    --do_train \
    --do_eval \
    --train_file /data/kyb0314/repos/kcc/transformer/train_file.json \
    --validation_file /data/kyb0314/repos/kcc/transformer/train_file.json \
    --source_prefix "난독화 해독하기: " \
    --output_dir /data/kyb0314/repos/kcc/transformer/model_ob1_lr2e-5_ep3 \
    --overwrite_output_dir \
    --per_device_train_batch_size=4 \
    --per_device_eval_batch_size=4 \
    --predict_with_generate \
    --text_column obfuscation1 \
    --summary_column original_data \
    --learning_rate 2e-05
```

#learing_rate = 5e-05 / epoch = 3.0
```
python run_summarization.py \
    --model_name_or_path KETI-AIR/ke-t5-small-ko \
    --do_train \
    --do_eval \
    --train_file /data/kyb0314/repos/kcc/transformer/train_file.json \
    --validation_file /data/kyb0314/repos/kcc/transformer/train_file.json \
    --source_prefix "난독화 해독하기: " \
    --output_dir /data/kyb0314/repos/kcc/transformer/model_ob1_lr5e-5_ep3 \
    --overwrite_output_dir \
    --per_device_train_batch_size=4 \
    --per_device_eval_batch_size=4 \
    --predict_with_generate \
    --text_column obfuscation1 \
    --summary_column original_data \
    --learning_rate 5e-05
```

#learing_rate = 1e-04 / epoch = 3.0
```
python run_summarization.py \
    --model_name_or_path KETI-AIR/ke-t5-small-ko \
    --do_train \
    --do_eval \
    --train_file /data/kyb0314/repos/kcc/transformer/train_file.json \
    --validation_file /data/kyb0314/repos/kcc/transformer/train_file.json \
    --source_prefix "난독화 해독하기: " \
    --output_dir /data/kyb0314/repos/kcc/transformer/model_ob1_lr1e-4_ep3 \
    --overwrite_output_dir \
    --per_device_train_batch_size=4 \
    --per_device_eval_batch_size=4 \
    --predict_with_generate \
    --text_column obfuscation1 \
    --summary_column original_data \
    --learning_rate 1e-04
```

#learing_rate = 1e-04 / epoch = 2.0
```
python run_summarization.py \
    --model_name_or_path KETI-AIR/ke-t5-small-ko \
    --do_train \
    --do_eval \
    --train_file /data/kyb0314/repos/kcc/transformer/train_file.json \
    --validation_file /data/kyb0314/repos/kcc/transformer/train_file.json \
    --source_prefix "난독화 해독하기: " \
    --output_dir /data/kyb0314/repos/kcc/transformer/model_ob1_lr1e-4_ep2 \
    --overwrite_output_dir \
    --per_device_train_batch_size=4 \
    --per_device_eval_batch_size=4 \
    --predict_with_generate \
    --text_column obfuscation1 \
    --summary_column original_data \
    --learning_rate 1e-04 \
    --num_train_epochs 2.0
```

#learing_rate = 1e-04 / epoch = 4.0
```
python run_summarization.py \
    --model_name_or_path KETI-AIR/ke-t5-small-ko \
    --do_train \
    --do_eval \
    --train_file /data/kyb0314/repos/kcc/transformer/train_file.json \
    --validation_file /data/kyb0314/repos/kcc/transformer/train_file.json \
    --source_prefix "난독화 해독하기: " \
    --output_dir /data/kyb0314/repos/kcc/transformer/model_ob1_lr1e-4_ep4 \
    --overwrite_output_dir \
    --per_device_train_batch_size=4 \
    --per_device_eval_batch_size=4 \
    --predict_with_generate \
    --text_column obfuscation1 \
    --summary_column original_data \
    --learning_rate 1e-04 \
    --num_train_epochs 4.0
```


