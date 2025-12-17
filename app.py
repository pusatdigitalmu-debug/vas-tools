import pandas as pd
import streamlit as st

# ... kode lainnya ...

def show_excel_viewer():
    st.header("📄 Daftar Ongkos Kirim")
    
    # 1. Baca File Excel
    try:
        # Ganti 'daftar_ongkir.xlsx' dengan nama file asli Anda
        df = pd.read_excel("daftar_ongkir.xlsx")
        
        # 2. Tampilkan di Layar
        # use_container_width=True agar tabel menyesuaikan lebar layar HP
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        st.caption("Tips: Anda bisa klik header kolom untuk mengurutkan (Sort) atau perbesar tabel di pojok kanan atas.")
        
    except FileNotFoundError:
        st.error("File Excel tidak ditemukan. Pastikan file sudah di-upload ke GitHub/Folder Project.")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat membaca file: {e}")

# --- Cara Memanggilnya ---
# Masukkan ini di logika navigasi Anda, misal:
# if selected == "Cek Ongkir Excel":
#     show_excel_viewer()
