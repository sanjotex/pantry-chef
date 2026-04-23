import streamlit as st
import google.generativeai as genai

# 1. Configuração Visual da Página
st.set_page_config(page_title="Pantry Chef", page_icon="🍳", layout="centered")

st.title("🍳 Pantry Chef")
st.markdown("A inteligência artificial transformando sua despensa em **alta gastronomia**.")

# 2. Barra Lateral para a Chave da API (Segurança e Profissionalismo)
with st.sidebar:
    st.header("⚙️ Configurações")
    st.markdown("Para usar o app, insira sua chave do Google Gemini.")
    api_key = st.text_input("Sua Chave API:", type="password")
    st.markdown("[Pegue sua chave gratuitamente aqui](https://aistudio.google.com/)")

# 3. Interface do Usuário (A tela principal)
ingredientes = st.text_area("O que temos na geladeira hoje?", placeholder="Ex: Meia lata de creme de leite, frango, batata e queijo...")

# 4. A Lógica (Quando clica no botão)
if st.button("Gerar Receita Exclusiva", type="primary"):
    
    # Validações antes de chamar a IA
    if not api_key:
        st.error("⚠️ Por favor, insira sua Chave API na barra lateral esquerda.")
    elif not ingredientes:
        st.warning("⚠️ Digite alguns ingredientes primeiro!")
    else:
        try:
            # Conecta com a sua Chave
            genai.configure(api_key=api_key)
            modelo = genai.GenerativeModel('gemini-1.5-flash-latest')

            # O Comando para o Chef
            prompt = f"""
            Você é um chef de cozinha profissional e inovador. O usuário tem estes ingredientes: {ingredientes}.
            Crie uma receita maravilhosa.
            Responda em formato Markdown bem estruturado, com:
            - Um título criativo (Heading 2)
            - Tempo de preparo e Dificuldade (em negrito)
            - Lista de Ingredientes
            - Modo de Preparo numerado passo a passo
            - Uma 'Dica do Chef' no final.
            """

            # Efeito visual de carregamento
            with st.spinner("👨‍🍳 O Chef está criando o cardápio..."):
                resposta = modelo.generate_content(prompt)

            # Mostra o resultado lindo na tela
            st.success("Seu prato está servido!")
            st.markdown(resposta.text)

        except Exception as e:
            st.error(f"❌ Ops! Ocorreu um erro técnico: {e}")
