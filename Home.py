import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")
with col2:
    st.title("Francisco Bautista")
    content = """
        Cuento con los estudios finalizados en el Ciclo de Grado Superior como Técnico Superior en Automatización y Regulación en el Centro de Estudios Ave María San Cristóbal (Granada). 
        Esta formación me ha permitido obtener conocimientos técnico-prácticos de automatización industrial y mantenimiento eléctrico-electrónico, 
        incluyendo la programación y uso de los complejos y flexibles PLC´s (Siemens/Omron)
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        #st.write("[Source Code](https://pythonhow.com)")
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")