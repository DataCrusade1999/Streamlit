import streamlit as st
import numpy as np
import pandas as pd

#st.title('hi') <---Could Also Use This To Give Title
"""
Hi
Look I Created A DataFrame
"""
df=pd.DataFrame(np.array([[5,6,7],[1,2,3],[4,5,6]]),columns=['a','b','c'])
selectbox=st.sidebar.selectbox('Choose The Number You Want!',df['a'])
'You Selected:',selectbox
st.write(df)

#PLOTTING A FIGURE 
"""
Hey Look I Plotted Something
"""
chart_data=pd.DataFrame(np.random.randint(-4,9,size=(3,3)),columns=['line1','line2','line3'])


st.line_chart(chart_data)

#PLOTTING RANDOM DATA ON MAPS
""" 
Random Data On Map
"""
if st.checkbox('Show The Plot'):
    map_data = pd.DataFrame(
    np.random.randn(998, 2) / [1, 1] + [70.00, 140.4],
    columns=['lat', 'lon'])

    st.map(map_data)







