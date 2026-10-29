import streamlit as st

# --- CẤU HÌNH BẢO MẬT ĐĂNG NHẬP ---
st.set_page_config(page_title="Hệ thống Khảo thí Hóa học", page_icon="🧪", layout="wide")

def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    if st.session_state["password_correct"]:
        return True

    st.subheader("🔐 Đăng nhập hệ thống khảo thí")
    password = st.text_input("Nhập mật khẩu giáo viên:", type="password")
    if st.button("Đăng nhập"):
        # Lấy mật khẩu từ secrets.toml
        admin_pwd = st.secrets.get("passwords", {}).get("admin_password", "MatKhauGiaoVien2026")
        if password == admin_pwd:
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("❌ Mật khẩu chưa chính xác!")
    return False

if not check_password():
    st.stop()

# --- ĐỊNH NGHĨA CÁC TRANG ĐA TRANG (MULTIPAGE) ---
pg = st.navigation([
    st.Page("app.py", title="Trang chủ", icon="🏠"),
    st.Page("1_Trộn_Đề.py", title="Trộn Đề Hóa học", icon="🔀"),
    st.Page("2_In_Phiếu_PDF.py", title="In Phiếu OMR", icon="🖨️"),
    st.Page("3_Chấm_Thi.py", title="Chấm Thi tự động", icon="📷"),
])

pg.run()
