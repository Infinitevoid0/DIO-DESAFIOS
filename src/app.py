import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analize_credit_card

def configure_interface():
    st.title("Upload de Arquivos - Descubra se o documento é fake")
    uploaded_file = st.file_uploader("Escolha um arquivo: ", type =["png", "jpeg", "jpg" ])
    if uploaded_file is not None:
        fileName = uploaded_file.name
        blob_url = upload_blob(uploaded_file, fileName)
        if blob_url:
         st.write(f"Arquivo {fileName} enviado com sucesso para o blob storage!")
         credit_card_info = analize_credit_card(blob_url)
         show_imagem_validation(blob_url, credit_card_info)
        else:
         st.write(f"Arquivo {fileName} obteve um erro ao enviar para o blob storage!")

def show_image_and_validation():
    st.image(blob_url, caption="imagem enviada", use_column_width = True)
    st.write("resultado da verificação:")
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"h1 style='color: green; '>Cartão válido</h1>", unsafe_allow_html=True)
        st.write(f"Nome do Titular: {credit_card_info['card_name']}")
        st.write(f"Banco emissor: {credit_card_info['bank_name']}")
        st.write(f"Data de validade: {credit_card_info['expiry_date']}")
    else:
        st.markdown(f"h1 style='color: red; '>Cartão inválido</h1>", unsafe_allow_html=True)
        st.write("Este não é um cartao de credito valido.")

if __name__ == "__main__":
    configure_interface()
