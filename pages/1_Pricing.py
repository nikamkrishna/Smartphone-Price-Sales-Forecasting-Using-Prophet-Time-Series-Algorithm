import streamlit as st
import pandas as pd
import plotly.express as px



st.title('Pricing ')
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# Load the data into a DataFrame
df = pd.read_csv("D:/gsf/final_price_forcasting.csv")

# Define the brands and their corresponding models
brands = {
    'Xiaomi': ['redmi_note11pro', 'redmi_note10pro'],
    'Apple': ['iphone_13promax', 'iphone_13pro', 'iphone_12pro'],
    'Samsung': ['s22_ultra', 's22', 's21'],
    'Oppo': ['reno_7pro'],
    'Vivo': ['vivo_v23', 'vivo_v21']
}


# Add a drop-down menu for selecting the brand and model
brand = st.selectbox('Brand', list(brands.keys()))
model = st.selectbox('Model', brands[brand])

# Filter the DataFrame by brand and model
filtered_df = df[model]

# # Plot the data using Plotly Express
fig = px.line(filtered_df, x=filtered_df.index, y=model)
fig.update_layout(title=f'{brand} {model} Predictions', xaxis_title='Date', yaxis_title='Price')
st.plotly_chart(fig)
