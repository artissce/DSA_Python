# app.py
import streamlit as st
from views import linked_list_view

# Configuración básica
st.set_page_config(page_title="DSA Visualizer", layout="wide")

# Inicializamos la página actual en 'home' si no existe
if 'page' not in st.session_state:
    st.session_state.page = "home"

# --- LÓGICA DE NAVEGACIÓN ---

def ir_a_home():
    st.session_state.page = "home"
    st.rerun()

def ir_a_linked_list():
    st.session_state.page = "linked_list"
    st.rerun()

# --- VISTA: HOME ---
if st.session_state.page == "home":
    st.title("DSA Visualizer")
    st.markdown("### Select structure or algorithm that you want to visualize:")
    
    st.markdown("---")
    
    # create columns 
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("Lineal")
        if st.button("Linked List", use_container_width=True):
            ir_a_linked_list()
        
        # Future strcture
        st.button("📚 Stack (Pila)", disabled=True, use_container_width=True)
        st.button("🚶 Queue (Cola)", disabled=True, use_container_width=True)

    with col2:
        st.info("No lineal")
        st.button("🌳 Binary Tree", disabled=True, use_container_width=True)
        st.button("🕸️ Graph", disabled=True, use_container_width=True)

    with col3:
        st.info("Algorithms")
        st.button("🔎 Binary Search", disabled=True, use_container_width=True)
        st.button("⚡ Sorting", disabled=True, use_container_width=True)

# --- VISTA: LINKED LIST ---
elif st.session_state.page == "linked_list":
    # Botón para regresar
    if st.button("⬅️ Back to Home"):
        ir_a_home()
    
    # load views
    linked_list_view.show_view()