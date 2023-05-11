import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns



st.title('Sales Page')
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# Load the data
df = pd.read_csv("D:/gsf/final_sales_data.csv")
# Convert the date column to a datetime type
df['date'] = pd.to_datetime(df['date'])

# Set the date column as the index
df.set_index('date', inplace=True)


# Resample the data by week and sum up the sales for each phone model
weekly_sales = df.resample('W').sum()
weekly_sales = weekly_sales.iloc[1:]

# Define dictionary of brands and model
brands_models = {
    "Xiaomi": ["redmi_note11pro", "redmi_note10pro"],
    "Apple": ["iphone_13promax", "iphone_13pro", "iphone_12pro"],
    "Samsung": ["s22_ultra", "s21"],
    "Oppo": ["reno_7pro"],
    "Vivo": ["vivo_v23", "vivo_v21"]
}

# Create dropdowns for brand and model selection
selected_brand = st.selectbox("Select brand:", list(brands_models.keys()))
selected_model = st.selectbox("Select model:", brands_models[selected_brand])

# Filter the data based on selected brand and model
data = weekly_sales[selected_model]

# Plot the data
fig, ax = plt.subplots()
ax.bar(data.index, data.values)
ax.set_xlabel("Week")
ax.set_ylabel("Units-Sold")
ax.set_title(selected_model)

# Set y-axis limit based on maximum value in the data
ax.set_ylim(0, data.max() * 1.1)

# Display the plot
st.pyplot(fig)