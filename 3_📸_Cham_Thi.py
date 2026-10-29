import streamlit as st

st.set_page_config(page_title="Chấm Thi OMR", page_icon="🖨️", layout="wide")

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("⛔ Bạn chưa đăng nhập! Vui lòng quay lại Trang chủ để xác thực.")
    st.stop()

st.title("📸 Module Chấm Thi & Phân Tích AI")
st.info("Quét phiếu qua camera, tự động đọc mã QR, chấm điểm, lưu Google Sheets và cố vấn AI Gemini 2.5 Flash.")
