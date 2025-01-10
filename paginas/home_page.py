import streamlit as st
from utils import conn

def home():
    css = """
        <style> 

            body{
                padding: 0px;
            }
            img{
                width: 100vw;
                margin: 0px;
                
            }
            .st-emotion-cache-yw8pof{
                padding: 0px;
            }
            .stAppHeader{
               visibility: hidden;
            }
            .e14lo1l1{
                background-color: #000000;
                width: 30px;
                height: 30px;
            }
            .st-emotion-cache-1wbqy5l {
                display: none;
            }
            .st-emotion-cache-bm2z3a{
                background-color: none;
                margin-top: -16px;
            }
            .st-emotion-cache-w9jsfw{
                padding: 15px;
            }
            #bem-vindo{
                padding: 20px;
            }
        </style>
    """
    st.write(css, unsafe_allow_html=True)
    info = conn.ler_arquivo_json("info", "info.json")
    
    st.image(info[0]["logo"])
    
    st.write('# Bem-vindo!')
    texto = """
        O que é Lorem Ipsum?
        Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos, e vem sendo utilizado desde o século XVI, quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou para fazer um livro de modelos de tipos. Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto para a editoração eletrônica, permanecendo essencialmente inalterado. Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de Lorem Ipsum, e mais recentemente quando passou a ser integrado a softwares de editoração eletrônica como Aldus PageMaker
    """
    conn.efeito_digitacao(texto, vel=5)