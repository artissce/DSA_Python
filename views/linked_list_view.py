import streamlit as st
import graphviz
import inspect
from data_structures import linkedListSingly 

# Función auxiliar para mostrar complejidad bonita
def mostrar_complejidad(time_comp, space_comp, detail=""):
    st.markdown("---")
    st.markdown("##### 📊 Complexity Analysis")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"**Time:** ${time_comp}$")
    with c2:
        st.markdown(f"**Space:** ${space_comp}$")
    
    if detail:
        st.caption(detail)

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
            st.markdown("### 🧠 NeetCode Practice")
            st.caption("Select a problem to expand its details and controls.")

            # --- PROBLEMA 1: DETECCIÓN DE CICLOS ---
            # Todo vive dentro de este expander
            with st.expander("🟢 Linked List Cycle (NeetCode 141)"):
                st.markdown("**Problem:** Given `head`, determine if the linked list has a cycle in it.")
                
                # A. Test Case Controls
                st.info("🛠️ **Test Case Setup** (Use these to create a scenario)")
                c1, c2 = st.columns(2)
                with c1:
                    if st.button("☣️ Create Cycle", help="Connect tail to 2nd node", use_container_width=True):
                        # ... lógica create cycle ...
                        curr = st.session_state.ll_head
                        if curr and curr.next:
                            while curr.next: curr = curr.next
                            if st.session_state.ll_head.next: curr.next = st.session_state.ll_head.next 
                            else: curr.next = st.session_state.ll_head
                            st.warning("Cycle created!")
                            st.rerun()
                with c2:
                    if st.button("🚑 Break Cycle", help="Restore linearity", use_container_width=True):
                        st.session_state.ll_head = linkedListSingly.break_cycle(st.session_state.ll_head)
                        st.success("Cycle broken.")
                        st.rerun()

                # B. Run Solution
                st.markdown("---")
                if st.button("▶️ Run Solution", key="nc_cycle", use_container_width=True):
                    res = linkedListSingly.has_cycle(st.session_state.ll_head)
                    if res: st.error("Result: True (Cycle detected)")
                    else: st.success("Result: False (No cycle)")
                    st.session_state.code_to_show = inspect.getsource(linkedListSingly.has_cycle)

                # C. Complexity (Integrado aquí mismo)
                st.markdown("##### 📊 Complexity")
                c_time, c_space = st.columns(2)
                c_time.markdown("**Time:** $O(n)$")
                c_space.markdown("**Space:** $O(1)$")
                st.caption("*Floyd's Tortoise and Hare algorithm uses two pointers and constant space.*")


            # --- PROBLEMA 2: REVERTIR LISTA ---
            with st.expander("🟢 Reverse Linked List (NeetCode 206)"):
                st.markdown("**Problem:** Reverse the singly linked list in-place.")
                
                # Check de seguridad
                if linkedListSingly.has_cycle(st.session_state.ll_head):
                    st.warning("⚠️ Cannot reverse a cyclic list. Please fix it in the problem above first.")
                else:
                    if st.button("▶️ Run Solution", key="nc_reverse", use_container_width=True):
                        st.session_state.ll_head = linkedListSingly.reverse_list(st.session_state.ll_head)
                        st.session_state.code_to_show = inspect.getsource(linkedListSingly.reverse_list)
                        st.rerun()
                    
                    # Complexity
                    st.markdown("---")
                    st.markdown("##### 📊 Complexity")
                    c_time, c_space = st.columns(2)
                    c_time.markdown("**Time:** $O(n)$")
                    c_space.markdown("**Space:** $O(1)$")
                    st.caption("*Iterative approach. We flip pointers as we traverse once.*")

            # --- ROADMAP ---
            st.divider()
            st.caption("🚧 **Roadmap**")
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