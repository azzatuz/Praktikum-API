st.markdown("""
    <style>
        /* 🌈 Background Gradien Halus */
        body {
            background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);
            font-family: 'Poppins', sans-serif;
            color: #2c3e50;
        }

        /* ✨ Container Utama (Efek Glassmorphism) */
        .main {
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(10px);
            padding: 2.5rem;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.15);
            transition: 0.3s ease-in-out;
        }
        .main:hover {
            transform: translateY(-3px);
            box-shadow: 0 12px 40px rgba(0,0,0,0.2);
        }

        /* 📝 Judul */
        h1, h2, h3 {
            color: #1a237e;
            text-align: center;
            font-weight: 700;
            letter-spacing: 0.5px;
        }

        /* 🔍 Input URL */
        .stTextInput>div>div>input {
            border-radius: 12px;
            border: 2px solid #d1d9ff;
            padding: 12px 14px;
            transition: all 0.3s ease;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);
        }
        .stTextInput>div>div>input:focus {
            border-color: #5563DE;
            box-shadow: 0 0 6px rgba(85,99,222,0.4);
        }

        /* 🔘 Tombol Cek Situs */
        .stButton>button {
            width: 100%;
            background: linear-gradient(90deg, #5563DE, #5e7bff);
            color: white !important;
            border-radius: 12px;
            font-weight: 600;
            padding: 12px;
            border: none;
            letter-spacing: 0.5px;
            transition: all 0.3s ease-in-out;
            box-shadow: 0 4px 10px rgba(85,99,222,0.3);
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #4655cc, #3b4cd7);
            transform: scale(1.05);
            box-shadow: 0 6px 14px rgba(85,99,222,0.4);
        }

        /* 📦 Kotak Hasil */
        .result-box {
            background: rgba(240,243,255,0.9);
            border-left: 6px solid #5563DE;
            padding: 15px 18px;
            margin-top: 12px;
            border-radius: 12px;
            color: #2c3e50;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
            transition: transform 0.2s;
        }
        .result-box:hover {
            transform: translateX(3px);
        }

        /* 💡 Info Box */
        .info-box {
            background: rgba(255, 249, 196, 0.9);
            border-left: 6px solid #ffc107;
            padding: 15px;
            margin: 10px 0;
            border-radius: 12px;
            font-size: 0.95rem;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }

        /* ⚠ Pesan Peringatan */
        .stAlert {
            border-radius: 12px !important;
        }

        /* 🔽 Expander */
        .streamlit-expanderHeader {
            font-weight: 600;
            color: #1a237e;
            font-size: 1rem;
        }

        /* 📜 Riwayat */
        .result-box b {
            color: #1a237e;
        }

        /* 💬 Footer */
        footer {visibility: hidden;}
        footer:after {
            content: "Made with ❤ by Andi | Google Safe Browsing API";
            visibility: visible;
            display: block;
            position: relative;
            top: 20px;
            text-align: center;
            font-size: 13px;
            color: #34495e;
        }
    </style>
""", unsafe_allow_html=True)
