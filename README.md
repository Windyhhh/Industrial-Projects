<div align="center">

# 🏭 Industrial-Projects

### E-commerce customer behavior analytics.

Data cleaning, preprocessing and visualization over an e-commerce customer-behavior dataset.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.3-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)

</div>

---

**Industrial-Projects** is an e-commerce **customer-behavior analytics** project — cleaning and preprocessing raw customer data, then producing multi-perspective visualizations (category sales, city orders, device ratios, user clusters).

> [!NOTE]
> 中文项目：工业项目合集——电商客户行为数据分析：清洗、预处理与可视化。

---

## Quickstart

```bash
git clone https://github.com/Windyhhh/Industrial-Projects.git
cd Industrial-Projects

pip install pandas matplotlib seaborn

# Clean + preprocess
python data_preprocessing.py

# Analyze
python data_analysis.py
```

Results are rendered to `visualizations/`.

---

## Features

- **Data cleaning** — `data_preprocessing.py` over the customer-behavior CSV.
- **Multi-perspective analysis** — category, city, device, monthly sales, user clusters.
- **Visualization output** — PNG figures in `visualizations/`.

---

## Project Structure

```
Industrial-Projects/
├── data_preprocessing.py       # cleaning pipeline
├── data_analysis.py            # analysis
├── ecommerce_customer_behavior_dataset.csv
├── cleaned_ecommerce_data.csv
└── visualizations/             # generated charts
```

---

## License

MIT — free to use, modify and distribute.
