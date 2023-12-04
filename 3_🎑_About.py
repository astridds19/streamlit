import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import os


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

st.sidebar.success("Halaman ini berisi tentang cara mengantisipasi diri kita agar terhindar dari cyber crime dalam penggunaan Aplikasi Dating")

with st.container():
    original_title = '<p style="font-family:Courier; color:Green; font-size: 20px;">Waspadai Ancaman Data Privasi di Aplikasi Dating Online</p>'
    st.info("Aplikasi kencan daring atau dating apps saat ini kian populer. Makin banyak orang yang menggunakan aplikasi untuk mencari pasangan, terlebih semenjak situasi pandemi yang telah membatasi aktivitas fisik masyarakat luas.")
    st.markdown(original_title, unsafe_allow_html=True)

    image = Image.open('C:\streamlit\photo\onlinedating.jpg')
    st.image(image, caption=None)
    
    st.write("---")
    st.header("Tips Saat Kalian Menggunakan Aplikasi Dating Online")
    st.write(
            """
           - Jangan terlalu banyak membagikan informasi pribadi di profil kalian.
           - Jangan hubungkan akun media sosial lain ke profil.
           - Pilih lokasi secara manual jika memungkinkan.
           - Gunakan otentifikasi dua faktor, jika memungkinkan.
           - Gunakan messenger bawaan di aplikasi kencan. Pindah ke  platform lain jika kalian benar-benar percaya dengan mereka.
           - Gunakan solusi keamanan terpercaya di perangkat kalian. Sekarang ada banyak aplikasi pihak ketiga yang bisa memberikan perlindungan lebih.
           - Ajukan banyak pertanyaan. Jangan hanya mengandalkan informasi yang diberikan di profil online seseorang.
           - Gunakan internet sebagai alat untuk mencari informasi dan akun media sosial orang yang Anda ajak ngobrol.
           - Saat bercakap-cakap di situs kencan, hindari memberikan nomor pribadi atau email Anda sebelum benar-benar mengenal orang itu.
           - Gunakan fitur [Google Image Reverse](https://www.labnol.org/reverse/) untuk mengecek apakah foto yang digunakan asli atau palsu.
           - Cek kembali warna kulit, rambut, atau wajah seseorang dalam video tersebut. Biasanya video palsu akan menampilkan seseorang dengan wajah yang tampak lebih buram daripada gambar lingkungan di sekitarnya. Selain itu, fokus video juga terkadang terlihat tidak natural.
           - Cek pencahayaan video tersebut, apakah terlihat tidak natural? Perlu Kamu  ketahui bahwa seringkali algoritma deepfake akan tetap menggunakan pencahayaan dari video klip seseorang yang ingin ditambahkan. Jadi, pencahayaan akan terlihat tidak sesuai pencahayaan di video target.
           - Anda dapat mencermati kembali audio pada video tersebut karena deepfake seringkali menampilkan gerak mulut yang terlihat tidak natural. Hal ini banyak ditemukan terutama ketika video yang dimanipulasi menggunakan audio tidak diedit dengan baik.

            """
        )
    st.write("[Learn More >](https://www.allianz.co.id/explore/8-tips-agar-aman-dari-pencurian-data-pribadi-secara-online.html)")

    
    #horizontal menu
selected = option_menu(
        menu_title=None, #required
        options=["World", "Local"], #required
        icons=["cloud-download","house"], #optional
        menu_icon="cast", #optional
        default_index=0, #optional
        orientation="horizontal",
    )

if selected == "World":
    st.subheader(f"Data Pengguna di Dunia/{selected}")
    image = Image.open('C:\streamlit\photo\penggunaApp.png')
    st.image(image, caption=None)
if selected == "Local":
    st.subheader(f"Data Pengguna Tinder di Indonesia/{selected}")
    image = Image.open('C:\streamlit\photo\wtinder.png')
    st.image(image, caption=None)


footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #ECCCB2;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://www.facebook.com/astrid.priscill.1/" target="_blank">Pricillia Astrid</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)