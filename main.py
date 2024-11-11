import streamlit as st

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