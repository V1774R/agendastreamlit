import time
import streamlit as st
import os
import json

def append_to_json(file_path, new_data):
    if os.path.isfile(file_path):
        # Carrega o conteúdo existente do arquivo JSON
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Verifica se o arquivo JSON é uma lista
        if isinstance(data, list):
            # Adiciona os novos dados à lista existente
            data.append(new_data)
        else:
            # Se não for uma lista, cria uma nova lista com os dados existentes e os novos dados
            data = [data, new_data]
    else:
        # Se o arquivo não existir, cria uma nova lista com os novos dados
        data = [new_data]
    
    # Salva o conteúdo atualizado de volta no arquivo JSON
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def ler_arquivo_json(caminho, nome_arquivo):
    # Cria o caminho completo para o arquivo JSON
    caminho_completo = os.path.join(caminho, nome_arquivo)
    
    # Verifica se o arquivo existe
    if os.path.isfile(caminho_completo):
        # Abre e lê o conteúdo do arquivo JSON
        with open(caminho_completo, 'r', encoding='utf-8') as file:
            dados = json.load(file)
        return dados
    else:
        return f"O arquivo {caminho_completo} não existe."


def efeito_digitacao(msg, vel=30):
    display_area = st.empty()
    display_text = ""
    for char in msg:
        display_text += char
        display_area.write(f'## {display_text}')
        time.sleep(vel / 1000.0)
    return display_area

def iniciarPrimeiroAcesso():
    if "exibiu_mensagens" not in st.session_state:
        st.session_state.exibiu_mensagens = False

    msgs = [
        'Olá, seja bem vindo ao seu Novo App!',
        'Vamos configurar tudo para o seu primeiro acesso!',
        'Vou precisar de alguns dados para continuar...',
        'É só preencher os dados abaixo!'
    ]
    
    if not os.path.isfile("info/info.json"):
        if not st.session_state.exibiu_mensagens:
            for i, msg in enumerate(msgs):
                display_area = efeito_digitacao(msg, vel=30)
                time.sleep(1.4)  # Tempo adicional após exibir a mensagem
                if i != 3:
                    display_area.empty()
            
    else:
        st.write('O arquivo não existe')

    nome = st.text_input('Digite seu nome completo:', key='nome')
    empresa = st.text_input('Digite o nome da sua empresa:', key='empresa')
    logo = st.text_input('Digite a url da sua logo (opcional)', key='logo')
    st.session_state.exibiu_mensagens = True
    if st.button('Enviar'):
        novo_dado = {"nome": nome, "empresa": empresa, "logo": logo}
        append_to_json('info/info.json', novo_dado)
        st.success('Dados enviados com sucesso!')
        st.balloons()
        time.sleep(2)
        st.rerun()

