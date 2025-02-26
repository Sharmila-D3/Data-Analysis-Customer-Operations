# customer_analysis.py

import pandas as pd
from datetime import datetime
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================
# PART 1 - CUSTOMER SEGMENTATION
# ==========================

# Load customer,sales_data data
customers = pd.read_csv(r'C:\Users\91770\Desktop\Data_Analysis_Assignment\data\customers.csv')
sales_data = pd.read_csv(r'C:\Users\91770\Desktop\Data_Analysis_Assignment\data\sales_data.csv')

# Print customers, sales_data
print(customers.head())
print(sales_data.head())

#print customers, sales_data formates and data types
print(customers.info())
print(sales_data.info())

# Convert order_date to datetime
sales_data['order_date'] = pd.to_datetime(sales_data['order_date'])

#print customers, sales_data values
print(customers.head())
print(sales_data.head())

#print customers, sales_data formates and data types
print(customers.info())
print(sales_data.info())

#check order_date output
print(sales_data['order_date'].head())

# Load orders data
orders = pd.read_csv(r'C:\Users\91770\Desktop\Data_Analysis_Assignment\data\orders1.csv')
print(orders.head())
print(orders.columns)

# Aggregate metrics for customer segmentation using orders1.csv
customer_metrics = orders.groupby('customer_id').agg(
    total_spend = ('total_amount', 'sum'),
    order_count = ('order_id', 'count'),
    last_order = ('order_date', 'max')
).reset_index()

from datetime import datetime
today = datetime.today()
customer_metrics['recency'] = (today - pd.to_datetime(customer_metrics['last_order'])).dt.days

print(customer_metrics.head())

import pandas as pd
from datetime import datetime
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Load orders1.csv (ensure the path is correct)
orders = pd.read_csv(r'C:\Users\91770\Desktop\Data_Analysis_Assignment\data\orders1.csv')

# Display columns to confirm
print(orders.columns)  # Expected: ['order_id', 'customer_id', 'order_date', 'city', 'total_amount']

# Convert order_date to datetime
orders['order_date'] = pd.to_datetime(orders['order_date'])

# Aggregate customer metrics: total spend, order count, and last order date
customer_metrics = orders.groupby('customer_id').agg(
    total_spend=('total_amount', 'sum'),
    order_count=('order_id', 'count'),
    last_order=('order_date', 'max')
).reset_index()

# Calculate recency: days since last order
today = datetime.today()
customer_metrics['recency'] = (today - customer_metrics['last_order']).dt.days

print(customer_metrics.head())

# Prepare features for clustering: total_spend, order_count, and recency
features = customer_metrics[['total_spend', 'order_count', 'recency']]

# Scale the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Apply K-Means clustering (e.g., 3 clusters)
k = 3
kmeans = KMeans(n_clusters=k, random_state=42)
customer_metrics['cluster'] = kmeans.fit_predict(scaled_features)

# Check cluster distribution
print(customer_metrics['cluster'].value_counts())

# Visualize clusters: Total Spend vs. Order Count
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='total_spend', 
    y='order_count', 
    hue='cluster', 
    data=customer_metrics, 
    palette='viridis'
)
plt.title('Customer Segmentation: Total Spend vs. Order Count')
plt.xlabel('Total Spend')
plt.ylabel('Order Count')
plt.show()

# Convert order_date to Period and then to Timestamp
orders['order_month'] = orders['order_date'].dt.to_period('M')
orders['order_month'] = orders['order_month'].dt.to_timestamp()

# Aggregate revenue by month
monthly_revenue = orders.groupby('order_month')['total_amount'].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(x='order_month', y='total_amount', data=monthly_revenue, marker='o')
plt.title('Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.show()

# Extract the day of the week from order_date
orders['order_day'] = orders['order_date'].dt.day_name()

daily_orders = orders['order_day'].value_counts().reset_index()
daily_orders.columns = ['day', 'order_count']
print(daily_orders)

plt.figure(figsize=(8, 5))
sns.barplot(x='day', y='order_count', data=daily_orders, hue='day', palette='coolwarm')
plt.title('Orders by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Orders')
plt.legend([],[], frameon=False)  # This removes the legend
plt.show()

#visualise cluster: Recency vs. Total Spend
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='recency', 
    y='total_spend', 
    hue='cluster', 
    data=customer_metrics, 
    palette='plasma'
)
plt.title('Customer Segmentation: Recency vs. Total Spend')
plt.xlabel('Recency (Days Since Last Order)')
plt.ylabel('Total Spend')
plt.show()

cluster_summary = customer_metrics.groupby('cluster').mean()[['total_spend', 'order_count', 'recency']]
print(cluster_summary)

# Convert order_date to a monthly period and then to Timestamp for plotting
orders['order_month'] = orders['order_date'].dt.to_period('M').dt.to_timestamp()

# Aggregate revenue by month
monthly_revenue = orders.groupby('order_month')['total_amount'].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(x='order_month', y='total_amount', data=monthly_revenue, marker='o')
plt.title('Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.show()

# Extract the day name from order_date
orders['order_day'] = orders['order_date'].dt.day_name()

# Count the number of orders for each day
daily_orders = orders['order_day'].value_counts().reset_index()
daily_orders.columns = ['day', 'order_count']

plt.figure(figsize=(8, 5))
sns.barplot(x='day', y='order_count', data=daily_orders, hue='day', palette='coolwarm')
plt.title('Orders by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Orders')
plt.legend([],[], frameon=False)  # Remove legend if not needed
plt.show()

