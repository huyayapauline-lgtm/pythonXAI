import streamlit as st  # 匯入streamlit模組並重新命名為st

st.title("數字金字塔")
number = st.number_input("請輸入一個數字(1到9)", step=1, min_value=1, max_value=9)
for i in range(1, number + 1):
    st.write(str(i) * i)
