import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import fastavro
import time
import os

# Load sample data
df = pd.read_csv("data/sample.csv")

# CSV write & read
start = time.time()
df.to_csv("data/output.csv", index=False)
csv_write = time.time() - start

start = time.time()
_ = pd.read_csv("data/output.csv")
csv_read = time.time() - start

# Parquet write & read
table = pa.Table.from_pandas(df)
start = time.time()
pq.write_table(table, "data/output.parquet")
parquet_write = time.time() - start

start = time.time()
_ = pq.read_table("data/output.parquet").to_pandas()
parquet_read = time.time() - start

# Avro write & read
records = df.to_dict(orient="records")
def infer_avro_type(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return "int"
    elif pd.api.types.is_float_dtype(dtype):
        return "float"
    else:
        return "string"

schema = {
    "doc": "Schema",
    "name": "Sample",
    "namespace": "test",
    "type": "record",
    "fields": [
        {"name": col, "type": infer_avro_type(df[col].dtype)}
        for col in df.columns
    ]
}

start = time.time()
with open("data/output.avro", "wb") as out:
    fastavro.writer(out, schema, records)
avro_write = time.time() - start

start = time.time()
with open("data/output.avro", "rb") as fo:
    _ = [r for r in fastavro.reader(fo)]
avro_read = time.time() - start

# File sizes
def get_size(path):
    return os.path.getsize(path) / 1024  # KB

print("\n📊 Results:")
print(f"CSV:     Write={csv_write:.4f}s | Read={csv_read:.4f}s | Size={get_size('data/output.csv'):.2f}KB")
print(f"Parquet: Write={parquet_write:.4f}s | Read={parquet_read:.4f}s | Size={get_size('data/output.parquet'):.2f}KB")
print(f"Avro:    Write={avro_write:.4f}s | Read={avro_read:.4f}s | Size={get_size('data/output.avro'):.2f}KB")
