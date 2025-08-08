import streamlit as st

st.title("🍽️ 點餐機")

# ✅ 初始化購物籃
if "cart" not in st.session_state:
    st.session_state.cart = []

# ✅ 重新整理畫面（不清空）
if st.button("🔁 重新整理畫面"):
    st.write("準備重新整理...")
    st.rerun()

# ✅ 輸入餐點
new_item = st.text_input("請輸入你想點的餐點：")

if st.button("加入餐點"):
    if new_item.strip() != "":
        st.session_state.cart.append(new_item.strip())
        st.success(f"已加入：{new_item}")
        st.rerun()
    else:
        st.warning("請輸入餐點名稱")

# ✅ 顯示購物籃
st.subheader("🛒 購物籃")
if st.session_state.cart:
    for i, item in enumerate(st.session_state.cart):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"{i+1}. {item}")
        with col2:
            if st.button("刪除", key=f"del_{i}"):
                st.session_state.cart.pop(i)
                st.rerun()
else:
    st.info("目前購物籃是空的喔～")
