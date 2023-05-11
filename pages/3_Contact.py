import streamlit as st

st.title('Contact Us')
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)



st.write('Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus fugit expedita et corrupti non, aspernatur possimus officiis reprehenderit quibusdam iste maxime porro, repellendus libero reiciendis placeat sapiente. Dolore eius quod laudantium autem magni, neque rem saepe. Aliquam earum, quibusdam aut provident ad, nihil consectetur quod esse molestiae dolorum animi quae.')
st.write('Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus fugit expedita et corrupti non, aspernatur possimus officiis reprehenderit quibusdam iste maxime porro, repellendus libero reiciendis placeat sapiente. Dolore eius quod laudantium autem magni, neque rem saepe. Aliquam earum, quibusdam aut provident ad, nihil consectetur quod esse molestiae dolorum animi quae.')
