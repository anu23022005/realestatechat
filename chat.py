import streamlit as st
import google.generativeai as genai
import os

# Set the API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyC7DS7QJYaCtv2LdxgObkqY9f9QNuf5Yls"

# Initialize the Gemini AI client
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def get_real_estate_info(query):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([
        "You are a helpful assistant knowledgeable in real estate.",
        query
    ])
    return response.text

def main():
    st.title("Real Estate Query Chatbot")
    
    # Initialize session state for messages
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask a question about real estate"):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        response = get_real_estate_info(prompt)
            
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

    # Sidebar instructions
    st.sidebar.title("How to Use")
    st.sidebar.write("""
    This chatbot can answer questions about real estate. You can ask about:
    - Stamp duty
    - Property registration
    - RERA (Real Estate Regulatory Authority)
    - Property tax
    - Home loans
    - Rental agreements
    - Real estate market trends
    """)

if __name__ == "__main__":
    main()
