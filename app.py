import streamlit as st

# --- CẤU HÌNH GIAO DIỆN & BẢO MẬT ---
st.set_page_config(page_title="Hệ thống Khảo thí Hóa học", page_icon="🧪", layout="wide")

def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    if st.session_state["password_correct"]:
        return True

    st.subheader("🔐 Đăng nhập hệ thống khảo thí Hóa học")
    password = st.text_input("Nhập mật khẩu giáo viên:", type="password")
    if st.button("Đăng nhập"):
        admin_pwd = st.secrets.get("passwords", {}).get("admin_password", "MatKhauGiaoVien2026")
        if password == admin_pwd:
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("❌ Mật khẩu chưa chính xác!")
    return False

if not check_password():
    st.stop()

# --- ĐỊNH NGHĨA ĐIỀU HƯỚNG ĐA TRANG ---
pg = st.navigation([
    st.Page("app.py", title="Trang chủ", icon="🏠"),
    st.Page("1_Tron_De.py", title="Trộn Đề Hóa học", icon="🔀"),
    st.Page("2_In_Phieu_PDF.py", title="In Phiếu OMR", icon="🖨️"),
    st.Page("3_Cham_Thi.py", title="Chấm Thi tự động", icon="📷"),
])

pg.run()
