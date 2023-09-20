import streamlit as st
from PIL import Image
import io

# Ganti dengan tautan gambar langsung Anda dari Google Drive
left_logo = "https://drive.google.com/uc?export=view&id=1JN-Z1W0OLOgLP-K7rrfVf_I5QEYrs0oF"
right_logo1 = "https://drive.google.com/uc?export=view&id=16AXHy7hf_3wcpwDc8QJbmQb_Tiu3IcAr"
right_logo2 = "https://drive.google.com/uc?export=view&id=1tt1mP8xHn9ZeQx9NgXUmeyVexZq5JXOM"
right_logo3 = "https://drive.google.com/uc?export=view&id=1x3LijJFZevCwYeyOhrEDMKvUesP6Xfpg"

header_html = f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400&display=swap');

    .reportview-container {{
        background-color: #006400; /* Ini akan mengubah latar belakang keseluruhan aplikasi */
    }}

    .header-container {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        background-color: #006400; /* Warna latar belakang hijau tua */
        padding: 15px 25px; /* Penambahan padding */
        border-radius: 15px;  /* Membuat header dengan sudut melengkung */
        width: 100%;  /* Memastikan header memiliki lebar penuh */
        font-family: 'Roboto', sans-serif; /* Menggunakan font Roboto */
    }}

    .header-container img {{
        max-height: 50px;
        margin: 0 10px; /* Menambahkan sedikit jarak */
    }}

    .header-text {{
        flex-grow: 1;
        padding-left: 20px; /* Menambahkan sedikit jarak dari logo */
    }}

    .header-text h2 {{
        margin: 1; /* Menghapus margin default */
        font-weight: 300; /* Font lebih ringan */
        font-size: 14px; /* Menyesuaikan ukuran font */
        color: #FFD700;  /* Warna emas untuk judul */
    }}

    .header-text p {{
        margin-top: 5px; /* Mengurangi margin atas untuk mendekatkan kedua baris teks */
        font-weight: 300; /* Font lebih ringan */
        font-size: 12px; /* Menyesuaikan ukuran font */
        color: #FFD700;  /* Warna emas muda untuk teks */
    }}

    .header-right {{
        display: flex;
        align-items: center;
    }}
</style>

<div class="header-container">
    <img src="{left_logo}" alt="left-logo">
    <div class="header-text">
        <h2>Calculate Your Forest Parameters Using AI</h2>
        <p>Explore, Calculate, Understand</p>
    </div>
    <div class="header-right">
        <img src="{right_logo1}" alt="right-logo1">
        <img src="{right_logo2}" alt="right-logo2">
        <img src="{right_logo3}" alt="right-logo3">
    </div>
</div>
"""

st.markdown(header_html, unsafe_allow_html=True)

#batass................................................................

# Tulisan "Data Input"
st.markdown("<h2 style='text-align: center; font-weight: bold;'>CAIEO 1.0</h2>", unsafe_allow_html=True)
st.write ("## Data Input")
labels = ["Upload Image georeferenced map", "Upload Band red georeferenced map", "Upload Nir georeferenced map"]
keys = ["uploader1", "uploader2", "uploader3"]

uploaded_files = {}

for label, key in zip(labels, keys):
    uploaded_file = st.file_uploader(label, type=["jpg", "jpeg", "png", "tif"], key=key)
    if uploaded_file:
        uploaded_files[key] = uploaded_file

st.markdown("""
<style>
    #calculateButtonContainer .stButton>button {
        width: 100%;
        color: white;
        background-color: #006400;
        margin-left: center;
        margin-right: center;
        display: block;
    }

    /* Pastikan tombol upload tidak terpengaruh */
    .stButton>button {
        width: center;
        background-color: grey;  /* Warna default untuk tombol di Streamlit */
    }
</style>
""", unsafe_allow_html=True)

# Membuat kolom untuk tombol "Calculate"
col_calc, _ = st.columns([12,1])

# Tombol Calculate dengan ID CSS "calculateButtonContainer"
with col_calc.container():
    st.markdown('<div id="calculateButtonContainer">', unsafe_allow_html=True)
    if st.button("Calculate"):
        st.write("Dihitung")
    st.markdown('</div>', unsafe_allow_html=True)
    
st.write("\n This prototype only valid for the calculation at 10 x 10 m pixel size, Only developed for equatorial and monsoon climate in Indonesia. Out if those spesification, the calculation is not reliable")

st.write("## Preview Data")

for key, label in zip(keys, labels):
    if key in uploaded_files:
        try:
            # Membuka gambar dengan Pillow
            with Image.open(uploaded_files[key]) as img:
                # Mengonversi ke mode RGB
                img_rgb = img.convert("RGB")
                
                # Mengonversi image ke PNG
                img_byte_array = io.BytesIO()
                img_rgb.save(img_byte_array, format="PNG")
                
                # Menampilkan gambar di Streamlit
                st.image(img_byte_array.getvalue(), caption=label, use_column_width=True)
        except Exception as e:
            st.write(f"Error loading image: {e}")
    else:
        st.markdown(
            """
            <div style="border: 2px dashed gray; padding: 5px; display: flex; justify-content: center; align-items: center;">
                <i>Image will be displayed here after upload.</i>
            </div>
            """, 
            unsafe_allow_html=True
        )