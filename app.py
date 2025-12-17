import streamlit as st
import pandas as pd

# Atur tampilan halaman
st.set_page_config(page_title="Cek Ongkir", layout="wide")

st.title("🚚 Cek Ongkos Kirim")

try:
    # BACA FILE EXCEL
    # Pastikan nama file 'ongkir.xlsx' ada di folder yang sama (di GitHub)
    df = pd.read_excel("ongkir.xlsx")

    # FITUR CARI (Agar sales cepat ketik nama kecamatan)
    cari = st.text_input("🔍 Cari Kecamatan / Kota:", placeholder="Ketik disini...")

    if cari:
        # Filter data sesuai ketikan (tidak peduli huruf besar/kecil)
        mask = df.astype(str).apply(lambda x: x.str.contains(cari, case=False, na=False)).any(axis=1)
        df_tampil = df[mask]
    else:
        df_tampil = df

    # TAMPILKAN TABEL
    # use_container_width=True supaya pas di layar HP
    st.dataframe(df_tampil, use_container_width=True, hide_index=True, height=600)

except FileNotFoundError:
    st.error("⚠️ File 'ongkir.xlsx' tidak ditemukan. Upload file Excel ke GitHub sejajar dengan app.py")
except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
