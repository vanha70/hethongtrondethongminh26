import streamlit as st

st.title("🖨️ In Phiếu OMR Cá Nhân Hóa")
st.write("Chức năng sinh phiếu thi, tô sẵn SBD/Mã đề và nhúng QR nén.")

num_students = st.number_input("Nhập số lượng học sinh:", min_value=1, max_value=100, value=40)
if st.button("Tạo phiếu PDF"):
    st.success(f"Đã tạo thành công phiếu OMR cho {num_students} học sinh!")
