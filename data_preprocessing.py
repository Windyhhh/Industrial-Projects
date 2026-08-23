import pandas as pd
import numpy as np
import mysql.connector
from mysql.connector import Error

# 读取数据
df = pd.read_csv('ecommerce_customer_behavior_dataset.csv')

# 查看数据基本信息
print('数据基本信息：')
print(df.info())
print('\n数据前5行：')
print(df.head())

# 处理异常值 - 年龄>75的记录
df = df[df['Age'] <= 75]
print('\n处理后数据行数：', len(df))

# 查看是否有缺失值
print('\n缺失值情况：')
print(df.isnull().sum())

# 数据类型转换
# 将Date转换为日期类型
df['Date'] = pd.to_datetime(df['Date'])

# 连接MySQL数据库并导入数据（跳过，直接使用CSV文件进行分析）
print('\n跳过MySQL导入步骤，直接使用CSV文件进行分析')

# 保存清洗后的数据到CSV文件（可选）
df.to_csv('cleaned_ecommerce_data.csv', index=False)
print('\n清洗后的数据已保存到 cleaned_ecommerce_data.csv')
