import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Dữ liệu sinh viên
data = {
    'Họ tên': ['Nguyễn Văn A', 'Trần Thị B', 'Lê Văn C', 'Phạm Thị D', 'Hoàng Văn E',
               'Vũ Thị F', 'Đặng Văn G', 'Bùi Thị H', 'Đỗ Văn I', 'Nông Thị K'],
    'Chuyên cần': [9.0, 8.5, 10.0, 7.5, 8.0, 9.5, 6.0, 8.5, 9.0, 7.0],
    'Giữa kỳ': [7.5, 8.0, 9.0, 6.5, 7.0, 8.5, 5.5, 9.0, 7.5, 6.0],
    'Cuối kỳ': [8.0, 8.5, 9.5, 7.0, 7.5, 9.0, 6.5, 8.5, 8.0, 7.0]
}

df = pd.DataFrame(data)
df['Tổng kết'] = (0.20 * df['Chuyên cần'] + 0.30 * df['Giữa kỳ'] + 0.50 * df['Cuối kỳ']).round(2)

def xep_loai(diem):
    if diem >= 8.5: return "Giỏi"
    elif diem >= 7.0: return "Khá"
    elif diem >= 5.0: return "Trung bình"
    else: return "Yếu"

df['Xếp loại'] = df['Tổng kết'].apply(xep_loai)

# 2. Giao diện Web
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Bảng điểm
st.header("Bảng điểm sinh viên")
st.dataframe(df, use_container_width=True)

# Thống kê
st.header("Thống kê")
st.write(f"- **Điểm trung bình của lớp:** {df['Tổng kết'].mean():.2f}")
st.write(f"- **Số sinh viên đạt (>= 5.0):** {(df['Tổng kết'] >= 5.0).sum()} sinh viên")

st.write("- **Sinh viên điểm cao nhất:**")
st.dataframe(df[df['Tổng kết'] == df['Tổng kết'].max()][['Họ tên', 'Tổng kết']], hide_index=True)

st.write("- **Sinh viên điểm thấp nhất:**")
st.dataframe(df[df['Tổng kết'] == df['Tổng kết'].min()][['Họ tên', 'Tổng kết']], hide_index=True)

# Chọn sinh viên
st.header("Tra cứu thông tin sinh viên")
ten_sv = st.selectbox("Chọn sinh viên:", df['Họ tên'])
sv_chon = df[df['Họ tên'] == ten_sv].iloc[0]

st.write(f"**Chuyên cần:** {sv_chon['Chuyên cần']} | **Giữa kỳ:** {sv_chon['Giữa kỳ']} | **Cuối kỳ:** {sv_chon['Cuối kỳ']}")
st.write(f"**Điểm tổng kết:** {sv_chon['Tổng kết']} | **Xếp loại:** {sv_chon['Xếp loại']}")

# Biểu đồ
st.header("Biểu đồ điểm tổng kết")
fig, ax = plt.subplots()
ax.barh(df['Họ tên'], df['Tổng kết'], color="#5B9BD5")
ax.invert_yaxis()
st.pyplot(fig)

# Thông tin tác giả
st.caption("Người thực hiện: **Thới Gia Nguyên** | MSSV: **052208002941**")
