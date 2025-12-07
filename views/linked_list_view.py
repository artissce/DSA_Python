import streamlit as st
import graphviz
import inspect
from data_structures import linkedListSingly 

def dibujar_lista(head):
    dot = graphviz.Digraph()
    dot.attr(rankdir='LR')
    dot.attr('node', shape='circle', style='filled', fillcolor='#E0F7FA', fontname='Helvetica')
    
    # Manejo visual de ciclos para que Graphviz no explote
    visited = set()
    current = head
    idx = 0
    
    while current:
        node_id = str(id(current))
        
        if node_id in visited:
            # Detectamos ciclo visualmente
            dot.edge(str(id(prev)), node_id, color="red", label="Cycle")
            break
            
        visited.add(node_id)
        dot.node(node_id, str(current.val))
        
        if current.next:
            # Si el siguiente ya fue visitado, es un ciclo, lo manejamos en la siguiente iteración
            dot.edge(node_id, str(id(current.next)))
        else:
            null_id = f"null_{idx}"
            dot.node(null_id, "None", shape="square", fillcolor="lightgray")
            dot.edge(node_id, null_id)
        
        prev = current
        current = current.next
        idx += 1
        
        # Limite de seguridad por si hay ciclo infinito al dibujar
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

    col_controls, col_display = st.columns([1, 2])

    with col_controls:
        st.subheader("Controls")
        
        # --- ADD ---
        with st.expander("➕ Add Node", expanded=True):
            val_add = st.number_input("Value", value=0, key="add_input")
            if st.button("Append Node"):
                st.session_state.ll_head = linkedListSingly.append_node(st.session_state.ll_head, val_add)
                st.session_state.code_to_show = inspect.getsource(linkedListSingly.append_node)
                st.rerun()

        # --- DELETE ---
        with st.expander("🗑️ Delete Operations"):
            val_del = st.number_input("Value to delete", value=0, key="del_input")
            
            col_d1, col_d2 = st.columns(2)
            with col_d1:
                if st.button("Delete One"):
                    st.session_state.ll_head = linkedListSingly.delete_node(st.session_state.ll_head, val_del)
                    st.session_state.code_to_show = inspect.getsource(linkedListSingly.delete_node)
                    st.rerun()
            with col_d2:
                if st.button("Delete Occurrences"):
                    st.session_state.ll_head = linkedListSingly.delete_all_occurrences(st.session_state.ll_head, val_del)
                    st.session_state.code_to_show = inspect.getsource(linkedListSingly.delete_all_occurrences)
                    st.rerun()
            
            if st.button("Remove Duplicates"):
                st.session_state.ll_head = linkedListSingly.remove_duplicates(st.session_state.ll_head)
                st.session_state.code_to_show = inspect.getsource(linkedListSingly.remove_duplicates)
                st.rerun()

        # --- SEARCH ---
        with st.expander("🔍 Search"):
            val_search = st.number_input("Value to find", value=0, key="search_input")
            if st.button("Search"):
                found = linkedListSingly.search(st.session_state.ll_head, val_search)
                if found:
                    st.success(f"Value {val_search} found!")
                else:
                    st.error(f"Value {val_search} not found.")
                st.session_state.code_to_show = inspect.getsource(linkedListSingly.search)
                # No hacemos rerun() aquí para que se mantenga el mensaje de éxito/error

        # --- UTILS / CYCLE ---
        with st.expander("⚙️ Utils & Cycle"):
            if st.button("Reverse List"):
                st.session_state.ll_head = linkedListSingly.reverse_list(st.session_state.ll_head)
                st.session_state.code_to_show = inspect.getsource(linkedListSingly.reverse_list)
                st.rerun()
            
            st.divider()
            
            col_c1, col_c2 = st.columns(2)
            
            with col_c1:
                if st.button("☣️ Create Cycle"):
                    # Tu lógica actual para crear ciclo...
                    curr = st.session_state.ll_head
                    if curr and curr.next:
                        while curr.next:
                            curr = curr.next
                        # Hacemos que el último apunte al segundo (para que se note más)
                        if st.session_state.ll_head.next:
                             curr.next = st.session_state.ll_head.next 
                        else:
                             curr.next = st.session_state.ll_head
                        st.warning("Cycle created!")
                        st.rerun()

            with col_c2:
                # BOTÓN NUEVO
                if st.button("🚑 Break Cycle"):
                    st.session_state.ll_head = linkedListSingly.break_cycle(st.session_state.ll_head)
                    st.success("Cycle removed. List is linear again.")
                    st.rerun()
            
            if st.button("Detect Cycle"):
                has_cycle = linkedListSingly.has_cycle(st.session_state.ll_head)
                if has_cycle:
                    st.error("Cycle Detected! 🔄")
                else:
                    st.success("No cycle detected.")
                st.session_state.code_to_show = inspect.getsource(linkedListSingly.has_cycle)

    # --- VISUALIZATION AREA ---
    with col_display:
        st.subheader("Visualization")
        st.graphviz_chart(dibujar_lista(st.session_state.ll_head))
        
        st.divider() # Línea divisoria visual
        
        st.subheader("Executed Code")
        if st.session_state.code_to_show:
            st.code(st.session_state.code_to_show, language='python')
        else:
            st.info("Interact with the controls to see the code here.")