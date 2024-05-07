# Deciphering Obfuscated Accommodation Reviews in Korean using Language Models

```
python run_summarization.py \
    --model_name_or_path KETI-AIR/ke-t5-&{size}-ko \
    --do_train \
    --do_eval \
    --do_predict \
    --train_file /data/kyb0314/repos/kcc/transformer/train_file.json \
    --validation_file /data/kyb0314/repos/kcc/transformer/validation_file.json \
    --test_file /data/kyb0314/repos/kcc/transformer/test_file.json \
    --source_prefix "난독화 해독하기: " \
    --output_dir /data/kyb0314/repos/kcc/transformer/&{size}_model_ob${ob}_lr1e-04_ep10 \
    --overwrite_output_dir \
    --per_device_train_batch_size=4 \
    --per_device_eval_batch_size=4 \
    --predict_with_generate \
    --text_column obfuscation${ob} \
    --summary_column original_data \
    --learning_rate 1e-04 \
    --num_train_epochs 10 \
    --save_total_limit 1
```

