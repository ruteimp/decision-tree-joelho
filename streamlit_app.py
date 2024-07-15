import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

# Estrutura da árvore de decisão
decision_tree = {
    'start': {'question': 'Você gosta de programação?', 'yes': 'programming', 'no': 'other'},
    'programming': {'question': 'Você prefere frontend ou backend?', 'frontend': 'frontend', 'backend': 'backend'},
    'frontend': {'question': 'Você prefere React ou Angular?', 'React': 'react', 'Angular': 'angular'},
    'backend': {'question': 'Você prefere Python ou Java?', 'Python': 'python', 'Java': 'java'},
    'other': {'question': 'Você gosta de outra área?', 'yes': 'other_yes', 'no': 'other_no'}
    # Adicione mais nós conforme necessário
}

# Função para percorrer a árvore
def traverse_tree(node):
    if node not in decision_tree:
        st.write("Fim da Árvore")
        return
    question_data = decision_tree[node]
    question = question_data['question']
    st.write(question)
    for option in question_data:
        if option != 'question':
            if st.button(option):
                st.session_state.current_node = question_data[option]
                st.experimental_rerun()

# Inicialização do estado da sessão
if 'current_node' not in st.session_state:
    st.session_state.current_node = 'start'

# Interface do Streamlit
st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
traverse_tree(st.session_state.current_node)
