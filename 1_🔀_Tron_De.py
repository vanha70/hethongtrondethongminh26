import streamlit as st

st.title("🔀 Trộn Đề Thi Hóa Học")
st.write("Chức năng xáo trộn mã đề, giữ nguyên định dạng MathType và tạo QR đáp án.")

uploaded_file = st.file_uploader("Tải lên tệp đề thi (Word/PDF):", type=["docx", "pdf"])
if uploaded_file is not None:
    st.success("Đã tải tệp lên thành công! Hệ thống đang xử lý trộn đề...")
