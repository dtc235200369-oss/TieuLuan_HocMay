import pandas as pd

# Đường dẫn trực tiếp tới file Parquet đã được Hugging Face chuyển đổi sẵn
base_url = "https://huggingface.co/datasets/uitnlp/vietnamese_students_feedback/resolve/refs%2Fconvert%2Fparquet/default"

df_train = pd.read_parquet(f"{base_url}/train/0000.parquet")
df_val = pd.read_parquet(f"{base_url}/validation/0000.parquet")
df_test = pd.read_parquet(f"{base_url}/test/0000.parquet")

# Lưu thành định dạng CSV vào thư mục data/
df_train.to_csv("data/train_feedback.csv", index=False)
df_val.to_csv("data/val_feedback.csv", index=False)
df_test.to_csv("data/test_feedback.csv", index=False)

print(f"Tải thành công! Số dòng -> Train: {len(df_train)}, Val: {len(df_val)}, Test: {len(df_test)}")