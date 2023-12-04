import streamlit as st
from PIL import Image 
import base64

st.set_page_config(
    page_title="Home",
    page_icon="🏘️",
)

st.warning("# 📲 Pentingnya Keamanan Siber dalam _Dating Application_ ‼️ ")
st.text("Internet sudah menjadi kehidupan kedua kita sehingga kita perlu memperhatikan keamanan data kita \n agar tidak disalahgunakan oleh pihak tertentu.")

image = Image.open('C:\streamlit\photo\komputer.jpg')
st.image(image, caption=None, width=800)

st.sidebar.success("Halaman ini berisi informasi umum mengenai Cyber Security dan Dating Application (Aplikasi Kencan Daring)")

st.write("---")
st.subheader("🔰 Apa Itu Cyber Security?")
st.markdown(
    """
    **Cyber security** adalah aktivitas yang dilakukan sistem atau seseorang dalam rangka melindungi sistem komputer dari serangan. Biasanya serangan tersebut bersifat ilegal. 
    Perlindungan dapat berupa perangkat lunak (_software_), aplikasi atau apa pun yang berhubungan dengan sistem komputer. Sehingga, dengan menggunakan keamanan siber, perusahaan dapat menanggulangi ancaman di sistem komputer.
     #### Awas, Ancaman Cyber Security ❗️❗️
    - **Cyber Crime** yaitu Manipulasi data, transaksi data secara ilegal, hingga pengrusakan pada sistem komputer. 
    - **Cyber Attack** biasanya terjadi kepada perusahaan dengan nama besar atau ada kepentingan politik. Tujuannya hampir sama yaitu menciptakan kerusuhan atau mencari keuntungan. Namun, yang paling berbahaya adalah mencuri data.  
    - **Cyber Terrorism** yakni jika serangan siber sampai menimbulkan ketakutan yang amat akut bahkan menciptakan kepanikan massal. 
"""
)


st.write("---")
with st.container():
    original_title = '<p style="font-family:Fantasy; color:Green; font-size: 20px;">Aplikasi Kencan Daring</p>'
    st.markdown(original_title, unsafe_allow_html=True)

 #"""### gif from local file"""
    file_ = open("/streamlit/photo/onlinedating.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
        )

    st.write("Kencan daring dapat dideskripsikan sebagai salah satu contoh aktivitas Computer Mediated Communication (CMC) yang dibuat secara sengaja untuk menemui orang-orang baru dan ditujukan untuk mendapatkan pasangan. Pada proses kencan daring, seseorang mendaftarkan dirinya secara daring melalui aplikasi. Setelah terdaftar, pengguna mengirimkan foto dan memasukkan setiap informasi yang ingin diketahui komunitas kencan daring tentang dirinya. Jika pengguna lain tertarik, mereka dapat saling mengirim pesan, emotikon, mengirim gambar, hingga panggilan video, untuk mengungkapkan adanya ketertarikan untuk saling mengenal.")

st.write("---")
with st.container():
    original_title = '<p style="font-family:Fantasy; color:Green; font-size: 20px;">Cari Jodoh di Dating Apps? Kenali Risikonya! </p>'
    st.markdown(original_title, unsafe_allow_html=True)

st.info(
"Aksi penipuan dan 'ghosting' lewat dating apps umumnya bisa dikenali lewat sejumlah 'red flags'. Di antaranya, tak lain janji manis yang terlalu banyak disampaikan meski perkenalan baru hitungan hari. \n Baru ketemu atau baru kenal sebulan (atau) dua bulan, tapi sudah janji menikah. Sudah janji A, B, C, atau baru kenal dua-tiga hari sudah janji mau ketemuin dengan orangtua."
"Pada beberapa kasus, penipu berani meminta banyak hal, atau meminta tolong secara tidak wajar di awal perkenalan, seperti pinjam uang, minta kuota internet, dsb. Seringkali, penipu membuat korban merasa bersalah jika keinginannya tak terpenuhi." 
"Kondisi inilah yang membuat korban kerap sulit menolak tipu daya penipu di dating apps."
)

st.write("---")
original_title ='<p style="font-family:Fantasy; color:Green; font-size: 20px;">Silakan Simak Video di bawah ini!</p>' 
st.markdown(original_title, unsafe_allow_html=True)

st.video("https://www.youtube.com/watch?v=_Z85Amrj3Xc")

#membuat footer
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

