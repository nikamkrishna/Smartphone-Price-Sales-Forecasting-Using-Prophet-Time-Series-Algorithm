import streamlit as st

st.set_page_config(
    page_title="Gadgets Sales forecasting",
    layout="wide",
    
)
st.title('Gadgets Sales Forecasting')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.image('./GSF/Ellipse.png')
st.image('./GSF/Other_19.png',width=420 )
st.image('./GSF/Ellipse_2.png')



st.write('This sales forecasting website helps in giving a clear view of sales data.')
st.write('It provides statistical analysis data which may not be  100%  accurate ')
