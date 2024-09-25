import streamlit as st
import random
from fun import get_voteless_combination, update_elo
import pandas as pd

st.set_page_config(initial_sidebar_state="collapsed")

st.title('Namen')


if 'namen' not in st.session_state:
    
    namen = []
    with open("namen.txt", "r") as file:
        while True:
            content=file.readline()
            if not content:
                break
            else:
                namen.append(content.split('.')[1].split('\n')[0])
    
    st.session_state['namen'] = namen
    st.session_state['rankings'] = {x:1000 for x in namen}
    st.session_state['choices'] = [
        
        ]
    st.session_state['active_combi'] = random.choice(namen), random.choice(namen)
     
st.write(f'Keuze {len(st.session_state["choices"])+1}') 
    
with st.sidebar:
     #st.write(st.session_state['choices'])
    df = pd.Series(st.session_state['rankings'])
    df.sort_values(inplace=True, ascending=False)
    st.subheader('Top 10')
    st.table(df.head(10))
    st.subheader('Bottom 5')
    st.table(df.tail(5))



choice_dict = {'name1':st.session_state['active_combi'][0], 'name2':st.session_state['active_combi'][1]}    
    
cols = st.columns([1,1,1,1,1,1])

with cols[0]:
    if st.button(label=st.session_state['active_combi'][0]):
        choice_dict['score'] = 1
        st.session_state['choices'].append(choice_dict)
        update_elo(st.session_state['rankings'], name_1=st.session_state['active_combi'][0], name_2=st.session_state['active_combi'][1], score_1=1)
        st.session_state['active_combi'] = get_voteless_combination(namen=st.session_state['namen'],choices=st.session_state['choices'])
        st.rerun() 
    
with cols[1]:
    if st.button(label='🤷‍♂️'):
        choice_dict['score'] = 0.5
        st.session_state['choices'].append(choice_dict)
        update_elo(st.session_state['rankings'], name_1=st.session_state['active_combi'][0], name_2=st.session_state['active_combi'][1], score_1=0.5)
        st.session_state['active_combi'] = get_voteless_combination(namen=st.session_state['namen'],choices=st.session_state['choices'])  
        st.rerun() 
       
with cols[2]:
    if st.button(label=st.session_state['active_combi'][1]):
        choice_dict['score'] = 0
        st.session_state['choices'].append(choice_dict)
        update_elo(st.session_state['rankings'], name_1=st.session_state['active_combi'][0], name_2=st.session_state['active_combi'][1], score_1=0)
        st.session_state['active_combi'] = get_voteless_combination(namen=st.session_state['namen'],choices=st.session_state['choices'])  
        st.rerun() 
        
st.write()