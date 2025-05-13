
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- LOAD DATA ---
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_sales_data.csv")
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Month'] = df['Order Date'].dt.to_period('M').astype(str)
    return df

df = load_data()

# --- HEADER ---
st.title("🛍️ Retail Sales Dashboard")
st.markdown("Visual analysis of sales performance")

# --- METRICS ---
total_sales = df['Sales'].sum()
avg_sales = df['Sales'].mean()
total_orders = df['Order ID'].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Sales", f"${total_sales:,.0f}")
col2.metric("📦 Avg Sale", f"${avg_sales:,.0f}")
col3.metric("🧾 Total Orders", total_orders)

# --- TOP PRODUCTS ---
st.subheader("🏆 Top 5 Products by Sales")
top_products = df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(5)

fig1, ax1 = plt.subplots()
top_products.plot(kind='bar', ax=ax1, color='skyblue')
ax1.set_ylabel("Sales ($)")
ax1.set_title("Top Products")
st.pyplot(fig1)

# --- SALES BY REGION ---
st.subheader("🌍 Sales by Region")
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

fig2, ax2 = plt.subplots()
region_sales.plot(kind='bar', ax=ax2, color='orange')
ax2.set_ylabel("Sales ($)")
ax2.set_title("Sales by Region")
st.pyplot(fig2)

# --- MONTHLY TREND ---
st.subheader("📈 Monthly Sales Trend")
monthly_sales = df.groupby('Month')['Sales'].sum()

fig3, ax3 = plt.subplots()
ax3.plot(monthly_sales.index, monthly_sales.values, marker='o', color='green')
ax3.set_ylabel("Sales ($)")
ax3.set_xlabel("Month")
ax3.set_title("Monthly Sales Trend")
plt.xticks(rotation=45)
st.pyplot(fig3)
