import streamlit as st

st.set_page_config(page_title="In Phiếu OMR", page_icon="🖨️", layout="wide")

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("⛔ Bạn chưa đăng nhập! Vui lòng quay lại Trang chủ để xác thực.")
    st.stop()

st.title("🖨️ Module Sinh Phiếu Thi PDF")
st.info("Tự động vẽ phiếu OMR chuẩn, tô sẵn SBD/Mã đề từ danh sách Excel và nhúng QR nén đáp án.")
