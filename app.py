import streamlit as st 

st.title('Welcome to Streamlit')

# inputs

m1 = st.text_input('Enter Your Input')
st.markdown(m1)

m2 = st.text_area('Enter Your Input')
st.markdown(m2)

st.warning('Please Enter Your Input')

st.success('Updated Successfully')

m3 = st.selectbox('Please Select ',['Python','Java','SQL'])
st.markdown(m3)

m4 = st.multiselect('Please Select ',['Python','Java','SQL'])
st.markdown(m4)

st.radio('Please Select ',['Python','Java','SQL'])

st.sidebar.text_input('Enter Your Name')
st.sidebar.selectbox('Please Select ',['Python','Java','SQL'])
st.sidebar.radio('Please Select ',['Python','Java','SQL'])
