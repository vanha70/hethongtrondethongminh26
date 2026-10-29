import streamlit as st

st.set_page_config(page_title="Trộn Đề Thi", page_icon="🔀", layout="wide")

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("⛔ Bạn chưa đăng nhập! Vui lòng quay lại Trang chủ để xác thực.")
    st.stop()

st.title("🔀 Module Trộn Đề Thi Hóa Học")
st.info("Tính năng xáo trộn mã đề, giữ nguyên định dạng MathType và sinh chuỗi JSON nén đáp án.")
