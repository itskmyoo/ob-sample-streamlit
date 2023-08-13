import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Load sample sales dataset
data_url = "sample_sales_data.csv"
data = pd.read_csv(data_url)



# App title
st.title("Interactive Sales Dashboard")

# Sidebar widgets
selected_product = st.sidebar.selectbox("Select Product:", data["Product"].unique())
selected_start_date = st.sidebar.date_input("Start Date:")
selected_end_date = st.sidebar.date_input("End Date:")

# cast the column to datatime and sort
data['Date'] = pd.to_datetime(data['Date'])
data = data.sort_values(by='Date')

# Define your date range
start_date = pd.to_datetime(selected_start_date)
end_date = pd.to_datetime(selected_end_date)


# Select data within the date range
filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

# Filter data based on product selection from widget
filtered_data = filtered_data[(filtered_data["Product"] == selected_product)]



# Create a line chart showing revenue trends
fig, ax = plt.subplots()
ax.plot(filtered_data["Date"], filtered_data["Revenue"], marker='o')
ax.set_xlabel("Month")
ax.set_ylabel("Revenue")
ax.set_title(f"Revenue Trend for {selected_product}")
plt.xticks(rotation=90)

st.pyplot(fig)

# Display filtered data in the table
st.write("Filtered Data:")
st.dataframe(filtered_data, width=1000)
