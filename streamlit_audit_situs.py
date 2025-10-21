import streamlit as st
import requests
import re

# Fungsi untuk memeriksa keamanan situs menggunakan Google Safe Browsing API
def cek_keamanan_situs(url):
    # Ambil API key dari secrets.toml
    try:
        API_KEY = st.secrets["API_KEY"]
    except KeyError:
        return {"error": "API key tidak ditemukan. Tambahkan di .streamlit/secrets.toml dengan format:\nAPI_KEY = 'your_api_key_here'"}

    # Jika pengguna tidak menulis http/https, tambahkan otomatis https://
    if not re.match(r"^https?://", url):
        url = "https://" + url

    # Validasi apakah input benar-benar URL website
    pola_url = re.compile(
        r"^https?://"  # Harus diawali http atau https
        r"(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}"  # domain.tld (misal uin-suka.ac.id)
        r"(?:/.*)?$"  # boleh ada path setelah domain
    )

    if not pola_url.match(url):
        return {"error": "Input tidak valid. Harap masukkan URL website yang benar (contoh: https://uin-suka.ac.id)"}

    ENDPOINT = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}"

    payload = {
        "client": {
            "clientId": "audit-situs-app",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": [
                "MALWARE",
                "SOCIAL_ENGINEERING",
                "UNWANTED_SOFTWARE",
                "POTENTIALLY_HARMFUL_APPLICATION"
            ],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }

    try:
        response = requests.post(ENDPOINT, json=payload, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return {"error": f"Permintaan ke API gagal: {str(e)}"}
    except Exception as e:
        return {"error": f"Terjadi kesalahan: {str(e)}"}


# UI Streamlit
st.set_page_config(page_title="Audit Keamanan Situs Web", page_icon="🔍")
st.title("🔍 Audit Keamanan Situs Web")
st.write("Masukkan URL situs yang ingin kamu cek keamanannya menggunakan Google Safe Browsing API.")

# Input URL
url = st.text_input("Masukkan URL situs (contoh: uin-suka.ac.id atau https://uin-suka.ac.id)")

# Tombol cek keamanan
if st.button("Cek Keamanan"):
    if not url.strip():
        st.warning("⚠️ Silakan masukkan URL terlebih dahulu.")
    else:
        hasil = cek_keamanan_situs(url.strip())

        if "error" in hasil:
            st.error(f"Gagal memeriksa: {hasil['error']}")
        elif not hasil.get("matches"):  # hasil kosong berarti aman
            st.success("✅ Situs aman menurut Google Safe Browsing API.")
        else:
            st.error("🚨 Situs terdeteksi berbahaya!")
            st.json(hasil)
