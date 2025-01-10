import streamlit as st
from paginas import home_page, agendamento_page
from utils import conn
import os
from streamlit_option_menu import option_menu

if os.path.isfile("info/info.json"):
    # pagina = st.radio("Menu de navegação", ["Inicio", "Agendamento"])
    
    # Cria o menu de navegação usando streamlit-option-menu
    with st.sidebar:
        pagina = option_menu("Menu", ["Página Inicial", "Agendamento", "Sobre", "Contato"],
                        icons=["house", "calendar", "info", "envelope"], menu_icon="cast", default_index=0)

    
    if pagina == "Página Inicial":
        home_page.home()
    elif pagina == "Agendamento":
        agendamento_page.agendamento()
    elif pagina == "Contato":
        #https://wa.me/5591982110851?text=olá,%20vim%20do%20app!%20Gostaria%20de%20mais%20informações.
        pass
    elif pagina == "Sobre":
        pass
else:
    conn.iniciarPrimeiroAcesso()






