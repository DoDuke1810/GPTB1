import streamlit as st

st.title('Giải phương trình bậc nhất')

st.balloons()
st.snow()
number1 = st.number_input('Tham số a')
number2 = st.number_input('Tham số b')

if st.button('Giải'):
	st.write('Phương trình có 1 nghiệm', -number2/number1)

