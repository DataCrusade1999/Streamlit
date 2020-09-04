import streamlit as st
import time

#SQUARING NUMBERS


st.title("Squaring Numbers")
st.warning('Only For Numbers Between 1 to 100')
#st.info("This App Lets You Calculate Square Of Numbers")

x=list(range(1,100))
x=st.sidebar.slider(label='Choose A Number x')
if x<=100:
    'Starting a long computation...'
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.01)
    '...and now we\'re done!'
    st.write(x ,'squared is', x*x)
with st.spinner('Done Now ,Chill And Watch Balloons!'):
    time.sleep(2)
st.balloons()
time.sleep(2)
st.success("Done!")