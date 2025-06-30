# 🧪 File Format Showdown

Compare the most common data file formats — **CSV**, **Parquet**, and **Avro** — using Python.

This mini-project measures:
- ✅ Write time
- ✅ Read time
- ✅ File size
- ✅ Schema support

It's a quick and effective way to understand how file formats impact real-world data engineering pipelines.

---

## 📊 Output Results

Here are the actual results from my test using ~10,000 rows of sample data:

CSV: Write=0.0057s | Read=0.0035s | Size=319.21KB
Parquet: Write=0.0019s | Read=0.0180s | Size=137.53KB
Avro: Write=0.0062s | Read=0.0064s | Size=304.79KB

yaml
Copy
Edit

### 🧠 Interpretation

| Format   | File Size | Read Time | Write Time | Notes |
|----------|-----------|-----------|------------|-------|
| **CSV**  | 319 KB    | Fast      | Fast       | Easy to use, but large and lacks schema support |
| **Parquet** | 137 KB | Slower read | Very fast write | ✅ Best for analytics — compact and efficient |
| **Avro** | 304 KB    | Fast      | Medium     | ✅ Supports schema evolution — great for Kafka |

---

## 🚀 How to Run This

### 🧱 Step 1: Install Dependencies

pip install pandas pyarrow fastavro

📂 Step 2: Generate Sample Data
bash
Copy
Edit
python generate_sample_data.py

⚡ Step 3: Run Format Comparison
bash
Copy
Edit
python format_comparison.py

🧠 What You’ll Learn
Why Parquet is preferred in most data lake use-cases

When to use Avro (especially in streaming pipelines with Kafka)

Why CSV doesn’t scale beyond toy examples

📂 Project Structure


file-format-showdown/
├── data/
│   ├── sample.csv
│   ├── output.csv
│   ├── output.parquet
│   └── output.avro
├── generate_sample_data.py
├── format_comparison.py
└── README.md

🙌 Credits & Author
Built by Jugal Sheth as part of a Data Engineering project series.

![ChatGPT Image Jun 29, 2025, 07_16_11 PM](https://github.com/user-attachments/assets/88ebf258-cd6f-455b-b908-db68588ae7c7)

