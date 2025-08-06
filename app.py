import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("Nifty_Stocks.csv")

# Convert date column
df["Date"] = pd.to_datetime(df["Date"])

# Streamlit title
st.title("📈 Nifty Stocks Viewer")

# Category selection
categories = df["Category"].unique()
selected_category = st.selectbox("Select Category:", categories)

# Filter based on category
filtered_by_category = df[df["Category"] == selected_category]

# Symbol selection
symbols = filtered_by_category["Symbol"].unique()
selected_symbol = st.selectbox("Select Symbol:", symbols)

# Filter based on symbol
final_df = filtered_by_category[filtered_by_category["Symbol"] == selected_symbol]

# Display data table
st.dataframe(final_df)

# Plotting
fig, ax = plt.subplots(figsize=(15, 8))
sb.lineplot(x=final_df["Date"], y=final_df["Close"], ax=ax)
ax.set_title(f"{selected_symbol} Closing Price Over Time")
ax.set_xlabel("Date")
ax.set_ylabel("Close Price")

# Show plot in Streamlit
st.pyplot(fig)
