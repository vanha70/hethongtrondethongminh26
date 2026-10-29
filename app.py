import streamlit as st

st.set_page_config(page_title="Hệ Thống Khảo Thí Hóa Học", page_icon="🏫", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    st.markdown(
        """
        <style>
            [data-testid="stSidebar"] { display: none; }
        </style>
        """, 
        unsafe_allow_html=True
    )
    
    st.title("🔒 Cổng Đăng Nhập Giáo Viên")
    st.info("Hệ thống khảo thí Hóa học độc quyền - Thầy Nguyễn Văn Hà.")
    
    mat_khau_nhap = st.text_input("Nhập mật khẩu truy cập hệ thống:", type="password")
    
    if st.button("Đăng nhập", type="primary"):
        # Mật khẩu mặc định hoặc lấy từ secrets
        pwd = st.secrets.get("passwords", {}).get("admin_password", "MatKhauGiaoVien2026")
        if mat_khau_nhap == pwd:
            st.session_state["logged_in"] = True
            st.success("Đăng nhập thành công! Hệ thống đang tải...")
            st.rerun()
        else:
            st.error("Sai mật khẩu! Vui lòng thử lại.")
else:
    st.title("👋 Chào mừng Thầy Nguyễn Văn Hà và các Thầy Cô")
    st.markdown("""
    **Vui lòng chọn chức năng ở thanh menu bên trái để bắt đầu làm việc:**
    * 🔀 **Trộn Đề:** Xáo trộn mã đề, giữ nguyên định dạng MathType, tạo QR đáp án.
    * 🖨️ **In Phiếu PDF:** Sinh phiếu OMR cá nhân hóa, tô sẵn SBD/Mã đề và nhúng QR nén.
    * 📸 **Chấm Thi:** Quét phiếu OMR qua camera, tự động đọc QR, chấm điểm và đồng bộ Google Sheets.
    """)
    
    if st.button("Đăng xuất"):
        st.session_state["logged_in"] = False
        st.rerun()
