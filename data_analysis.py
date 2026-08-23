import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取清洗后的数据
df = pd.read_csv('cleaned_ecommerce_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

# 1. 用户行为分析
print('=== 1. 用户行为分析 ===')

# 1.1 各设备类型的订单占比
print('\n1.1 各设备类型的订单占比：')
device_order_count = df['Device_Type'].value_counts()
device_order_ratio = device_order_count / len(df) * 100
print(device_order_ratio)

# 1.2 各设备类型的平均会话时长
print('\n1.2 各设备类型的平均会话时长：')
device_session_duration = df.groupby('Device_Type')['Session_Duration_Minutes'].mean()
print(device_session_duration)

# 1.3 回头客比例
print('\n1.3 回头客比例：')
returning_customer_ratio = df['Is_Returning_Customer'].sum() / len(df) * 100
print(f'回头客比例：{returning_customer_ratio:.2f}%')

# 1.4 各城市订单数量
print('\n1.4 各城市订单数量：')
city_order_count = df['City'].value_counts()
print(city_order_count.head(10))  # 只显示前10个城市

# 2. 销售趋势分析
print('\n=== 2. 销售趋势分析 ===')

# 2.1 按月统计销售额趋势
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Total_Amount'].sum()
print('\n2.1 按月统计销售额趋势：')
print(monthly_sales)

# 2.2 各产品类别的销售额
print('\n2.2 各产品类别的销售额：')
category_sales = df.groupby('Product_Category')['Total_Amount'].sum().sort_values(ascending=False)
print(category_sales)

# 2.3 各产品类别的折扣率（折扣金额/总金额）
df['Discount_Rate'] = df['Discount_Amount'] / (df['Unit_Price'] * df['Quantity']) * 100
df['Discount_Rate'] = df['Discount_Rate'].fillna(0)  # 处理除以0的情况
category_discount_rate = df.groupby('Product_Category')['Discount_Rate'].mean()
print('\n2.3 各产品类别的平均折扣率：')
print(category_discount_rate)

# 2.4 各产品类别的平均评分
category_rating = df.groupby('Product_Category')['Customer_Rating'].mean()
print('\n2.4 各产品类别的平均评分：')
print(category_rating)

# 3. 用户分群与推荐策略
print('\n=== 3. 用户分群与推荐策略 ===')

# 3.1 基于年龄、消费金额、会话时长进行K-Means聚类
# 计算每个用户的总消费金额和平均会话时长
user_features = df.groupby('Customer_ID').agg({
    'Age': 'mean',
    'Total_Amount': 'sum',
    'Session_Duration_Minutes': 'mean'
}).reset_index()

# 数据标准化
scaler = StandardScaler()
scaled_features = scaler.fit_transform(user_features[['Age', 'Total_Amount', 'Session_Duration_Minutes']])

# 使用K-Means进行聚类（k=3）
kmeans = KMeans(n_clusters=3, random_state=42)
user_features['Cluster'] = kmeans.fit_predict(scaled_features)

# 分析各聚类的特征
print('\n3.1 各用户群的特征：')
cluster_analysis = user_features.groupby('Cluster').agg({
    'Age': ['mean', 'std'],
    'Total_Amount': ['mean', 'std'],
    'Session_Duration_Minutes': ['mean', 'std'],
    'Customer_ID': 'count'
}).round(2)
print(cluster_analysis)

# 4. 可视化
print('\n=== 4. 可视化 ===')

# 创建图表保存目录
import os
if not os.path.exists('visualizations'):
    os.makedirs('visualizations')

# 4.1 各设备类型的订单占比（饼图）
plt.figure(figsize=(8, 6))
device_order_ratio.plot(kind='pie', autopct='%.1f%%', startangle=90)
plt.title('各设备类型的订单占比')
plt.ylabel('')
plt.savefig('visualizations/device_order_ratio.png', dpi=300, bbox_inches='tight')
plt.close()

# 4.2 各设备类型的平均会话时长（柱状图）
plt.figure(figsize=(8, 6))
device_session_duration.plot(kind='bar')
plt.title('各设备类型的平均会话时长')
plt.xlabel('设备类型')
plt.ylabel('平均会话时长（分钟）')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('visualizations/device_session_duration.png', dpi=300, bbox_inches='tight')
plt.close()

# 4.3 各城市订单数量（柱状图，前10个城市）
plt.figure(figsize=(10, 6))
city_order_count.head(10).plot(kind='bar')
plt.title('各城市订单数量（前10）')
plt.xlabel('城市')
plt.ylabel('订单数量')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('visualizations/city_order_count.png', dpi=300, bbox_inches='tight')
plt.close()

# 4.4 按月销售额趋势（折线图）
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker='o')
plt.title('按月销售额趋势')
plt.xlabel('月份')
plt.ylabel('销售额')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('visualizations/monthly_sales.png', dpi=300, bbox_inches='tight')
plt.close()

# 4.5 各产品类别的销售额（柱状图）
plt.figure(figsize=(10, 6))
category_sales.plot(kind='bar')
plt.title('各产品类别的销售额')
plt.xlabel('产品类别')
plt.ylabel('销售额')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('visualizations/category_sales.png', dpi=300, bbox_inches='tight')
plt.close()

# 4.6 各产品类别的平均折扣率和平均评分（双轴图）
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()

width = 0.4
category_sales.index = category_sales.index.astype(str)
ax1.bar(category_sales.index, category_discount_rate[category_sales.index], width, label='平均折扣率', color='blue')
ax2.plot(category_sales.index, category_rating[category_sales.index], label='平均评分', color='red', marker='o')

ax1.set_title('各产品类别的平均折扣率和平均评分')
ax1.set_xlabel('产品类别')
ax1.set_ylabel('平均折扣率（%）', color='blue')
ax2.set_ylabel('平均评分', color='red')
ax1.tick_params(axis='x', rotation=45)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.tight_layout()
plt.savefig('visualizations/category_discount_rating.png', dpi=300, bbox_inches='tight')
plt.close()

# 4.7 用户分群可视化（散点图）
plt.figure(figsize=(10, 8))
sns.scatterplot(
    x='Total_Amount',
    y='Session_Duration_Minutes',
    hue='Cluster',
    size='Age',
    data=user_features,
    palette='viridis',
    alpha=0.7
)
plt.title('用户分群结果（基于消费金额、会话时长和年龄）')
plt.xlabel('总消费金额')
plt.ylabel('平均会话时长（分钟）')
plt.legend(title='用户群')
plt.tight_layout()
plt.savefig('visualizations/user_clusters.png', dpi=300, bbox_inches='tight')
plt.close()

# 5. 个性化推荐策略建议
print('\n=== 5. 个性化推荐策略建议 ===')
print('基于K-Means聚类结果，针对不同用户群的推荐策略：')

# 获取各聚类的中心特征（需要转换回原始尺度）
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)

for i in range(3):
    age_center, amount_center, session_center = cluster_centers[i]
    print(f'\n用户群 {i+1} 特征：')
    print(f'  - 平均年龄：{age_center:.1f} 岁')
    print(f'  - 平均消费金额：{amount_center:.1f}')
    print(f'  - 平均会话时长：{session_center:.1f} 分钟')
    
    if amount_center > user_features['Total_Amount'].mean() * 1.5 and session_center > user_features['Session_Duration_Minutes'].mean():
        print('  推荐策略：高端产品推荐，个性化定制服务，VIP专属优惠')
    elif amount_center < user_features['Total_Amount'].mean() and age_center < 30:
        print('  推荐策略：性价比产品，限时折扣，社交媒体营销')
    else:
        print('  推荐策略：热门产品推荐，个性化推荐算法，会员积分体系')

print('\n所有分析已完成，可视化图表已保存到 visualizations 目录')
