import streamlit as st

st.title("📷 Chấm Thi Tự Động OMR")
st.write("Quét phiếu OMR qua camera, tự động đọc QR, chấm điểm và đồng bộ Google Sheets.")

picture = st.camera_input("Chụp ảnh phiếu bài làm của học sinh")
if picture is not None:
    st.success("Đã nhận diện ảnh chụp và đang tiến hành chấm điểm tự động...")
