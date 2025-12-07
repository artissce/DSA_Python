import streamlit as st
import graphviz
import inspect
from data_structures import linkedListSingly 

def dibujar_lista(head):
    # --- LOGICA DE DIBUJO ---
    dot = graphviz.Digraph()
    dot.attr(rankdir='LR')
    dot.attr('node', shape='circle', style='filled', fillcolor='#E0F7FA', fontname='Helvetica')
    
    visited = set()
    current = head
    idx = 0
    prev = None 
    
    while current:
        node_id = str(id(current))
        
        if node_id in visited:
            # Ciclo detectado visualmente
            if prev:
                dot.edge(str(id(prev)), node_id, color="red", label="Cycle", penwidth="2.0")
            break
            
        visited.add(node_id)
        dot.node(node_id, str(current.val))
        
        if current.next:
            if str(id(current.next)) in visited:
                 # Es la arista que cierra el ciclo
                 dot.edge(node_id, str(id(current.next)), color="red", label="Cycle", penwidth="2.0")
            else:
                 dot.edge(node_id, str(id(current.next)))
        else:
            null_id = f"null_{idx}"
            dot.node(null_id, "None", shape="square", fillcolor="lightgray")
            dot.edge(node_id, null_id)
        
        prev = current
        current = current.next
        idx += 1
        
        if idx > 20: break 
    
    if not head:
        dot.node("Empty", "Empty List", shape="box", style="dashed")
    return dot

def show_view():
    st.header("🔗 Singly Linked List")

    # Inicializar estado
    if 'll_head' not in st.session_state:
        st.session_state.ll_head = None
    if 'code_to_show' not in st.session_state:
        st.session_state.code_to_show = ""

    # Layout: Columnas
    col_controls, col_display = st.columns([1, 2.5]) 

    # --- COLUMNA IZQUIERDA: CONTROLES ---
    with col_controls:
        st.subheader("Controls")
        
        with st.expander("➕ Add Node", expanded=True):
            val_add = st.number_input("Value", value=0, key="add_input")
            if st.button("Append Node", use_container_width=True):
                st.session_state.ll_head = linkedListSingly.append_node(st.session_state.ll_head, val_add)
                st.session_state.code_to_show = inspect.getsource(linkedListSingly.append_node)
                st.rerun()

        with st.expander("🗑️ Delete Operations"):
            val_del = st.number_input("Value to delete", value=0, key="del_input")
            if st.button("Delete One", use_container_width=True):
                st.session_state.ll_head = linkedListSingly.delete_node(st.session_state.ll_head, val_del)
                st.session_state.code_to_show = inspect.getsource(linkedListSingly.delete_node)
                st.rerun()
            if st.button("Delete All Occurrences", use_container_width=True):
                st.session_state.ll_head = linkedListSingly.delete_all_occurrences(st.session_state.ll_head, val_del)
                st.session_state.code_to_show = inspect.getsource(linkedListSingly.delete_all_occurrences)
                st.rerun()
            if st.button("Remove Duplicates", use_container_width=True):
                st.session_state.ll_head = linkedListSingly.remove_duplicates(st.session_state.ll_head)
                st.session_state.code_to_show = inspect.getsource(linkedListSingly.remove_duplicates)
                st.rerun()

        with st.expander("🔍 Search"):
            val_search = st.number_input("Find Value", value=0, key="search_input")
            if st.button("Search", use_container_width=True):
                found = linkedListSingly.search(st.session_state.ll_head, val_search)
                if found: st.toast(f"✅ Value {val_search} found!", icon="🎉")
                else: st.toast(f"❌ Value {val_search} not found.", icon="🚫")
                st.session_state.code_to_show = inspect.getsource(linkedListSingly.search)
            
            

    # --- COLUMNA DERECHA: DISPLAY ---
    with col_display:
        
        # 1. VISUALIZACION SIEMPRE ARRIBA
        st.subheader("Visualization")
        with st.container(border=True):
            st.graphviz_chart(dibujar_lista(st.session_state.ll_head), use_container_width=True)

        st.divider()

        # 2. PESTAÑAS
        tab_neet, tab_code = st.tabs(["🎓 NeetCode Challenges", "💻 Source Code"])

        with tab_neet:
            
            # --- SECCIÓN 1: DETECCIÓN DE CICLOS (NeetCode 141) ---
            st.markdown("#### 🟢 Linked List Cycle (NeetCode 141)")
            st.caption("Check if the current list has a cycle.")
            
            # 1. HERRAMIENTAS DE PRUEBA
            st.markdown("**1. Prepare Test Case:**")
            col_c1, col_c2 = st.columns(2)
            with col_c1:
                if st.button("☣️ Create Cycle", help="Point last node to second node", use_container_width=True):
                    curr = st.session_state.ll_head
                    if curr and curr.next:
                        while curr.next: curr = curr.next
                        if st.session_state.ll_head.next: curr.next = st.session_state.ll_head.next 
                        else: curr.next = st.session_state.ll_head
                        st.warning("Cycle created! (Last -> 2nd)")
                        st.rerun()
            with col_c2:
                if st.button("🚑 Break Cycle", help="Point last node to None", use_container_width=True):
                    st.session_state.ll_head = linkedListSingly.break_cycle(st.session_state.ll_head)
                    st.success("Cycle broken. List is linear.")
                    st.rerun()

            # 2. EJECUTAR SOLUCIÓN
            st.markdown("**2. Run Solution:**")
            if st.button("▶️ Run Check (Has Cycle?)", key="nc_cycle", use_container_width=True):
                res = linkedListSingly.has_cycle(st.session_state.ll_head)
                if res: st.error("Result: True (Cycle detected!)")
                else: st.success("Result: False (No cycle found)")
                st.session_state.code_to_show = inspect.getsource(linkedListSingly.has_cycle)

            st.divider()

            # --- SECCIÓN 2: REVERTIR LISTA (NeetCode 206) ---
            st.markdown("#### 🟢 Reverse Linked List (NeetCode 206)")
            st.caption("Reverses the list in place.")
            
            # PROTECCIÓN: Advertimos si hay ciclo antes de revertir
            if linkedListSingly.has_cycle(st.session_state.ll_head):
                st.warning("⚠️ Cannot reverse a cyclic list. Please 'Break Cycle' first.")
            else:
                if st.button("▶️ Run Solution (Reverse)", key="nc_reverse", use_container_width=True):
                    st.session_state.ll_head = linkedListSingly.reverse_list(st.session_state.ll_head)
                    st.session_state.code_to_show = inspect.getsource(linkedListSingly.reverse_list)
                    st.rerun()
            
            st.divider()
            
            # --- ROADMAP ---
            with st.expander("🚧 Roadmap: Future Implementations"):
                st.markdown("""
                These are the **NeetCode** patterns planned for the next release. 
                Feel free to contribute!
                """)
                st.checkbox("🟢 Middle of the Linked List (NeetCode 876)", value=False, disabled=True)
                st.checkbox("🟡 Remove Nth Node From End of List (NeetCode 19)", value=False, disabled=True)
                st.checkbox("🟢 Merge Two Sorted Lists (NeetCode 21)", value=False, disabled=True)
                st.checkbox("🟡 Sort List (Merge Sort) (NeetCode 148)", value=False, disabled=True)
                st.checkbox("🟢 Palindrome Linked List (NeetCode 234)", value=False, disabled=True)
                st.caption("*Checked items are currently in development.*")
                
        with tab_code:
            st.markdown("### Logic Executed")
            if st.session_state.code_to_show:
                st.code(st.session_state.code_to_show, language='python')
            else:
                st.caption("Perform any action to see the code here.")