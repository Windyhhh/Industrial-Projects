<div align="center">

# 工业工程项目合集 | Industrial-Projects

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


## Results

<div align="center">
  <img src="visualizations/monthly_sales.png" alt="Monthly sales" width="70%"/>
  <img src="visualizations/user_clusters.png" alt="User clusters" width="70%"/>
</div>

---
## 技术实现细节

### 架构概览

项目采用模块化设计，核心目录包括：**visualizations**。

### 技术栈与依赖

**核心框架/库**：NumPy, matplotlib, pandas, scikit-learn, seaborn

**主要 import**：
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os
import pandas as pd
import numpy as np
import mysql.connector
```

### 实现要点

- 基于 NumPy, matplotlib, pandas 构建，技术栈成熟稳定
- 代码结构清晰，模块间低耦合，便于扩展和维护

---
## License

MIT — free to use, modify and distribute.
