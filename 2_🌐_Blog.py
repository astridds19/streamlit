import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Blog",
    page_icon=":heart:",
    layout="wide"
)

st.info("# 💘 Pernahkah Kamu Melihat Aplikasi Dating Online?❓")
st.caption("Dating app atau aplikasi kencan online adalah platform yang memungkinkan penggunanya untuk mendapatkan teman chat, pasangan, atau teman kencan dengan melihat identitas masing-masing dan berkenalan melalui fitur chat. ")

image = Image.open('C:\streamlit\photo\DatingApp.jpg')
st.image(image, caption=None)

with st.container():
    original_title = '<p style="font-family:Papyrus; color:Blue; font-size: 20px;">Dating Application memungkinkan seseorang mengalami chatfishing, doxing, deepfake, dan digital dating abuse jika tidak berhati-hati. Simak di sini!</p>'
    st.markdown(original_title, unsafe_allow_html=True)


st.subheader("Apa Itu Digital Dating Abuse?")
st.markdown(
    """
    **Ikhsan Bella Persada, M.Psi., Psikolog**, menjelaskan digital dating abuse merupakan sebuah perilaku kekerasan yang bisa dilakukan via digital seperti teks (chat atau SMS) dan media sosial.
    Jadi, bukan kekerasan secara fisik seperti memukul, melainkan kekerasan yang dilakukan secara digital by phone atau online. 

    ### Ciri-Ciri Seseorang Melakukan Digital Dating Abuse
    - Masuk Akun Media Sosial Pasangan Tanpa Izin 
    - Mengancam Pasangan via Chat 
    - Menjatuhkan dan Membuat Korban Malu
    - Sengaja Mempublikasikan Hal Pribadi ke Media Sosial 
"""
)


tab1, tab2, tab3, tab4 = st.tabs(["CHAT", "DOXING", "PERETASAN", "VIDEO"])

with tab1:
    st.header("Contoh Digital Abuse")  
    image = Image.open('C:\streamlit\photo\digital_abuse.jpg')
    st.image(image, caption='Gambar 1. Chat yang berisi digital abuse', width=400)

with tab2:
    st.header("Doxing")
    image = Image.open('C:\streamlit\photo\doxing.jpg')
    st.image(image, caption='Gambar 2. Doxing', width=400)

with tab3:
    st.header("Peretasan Akun Whatsapp")
    st.markdown("""
    - [See more...](https://android62.com/cara-membajak-wa-whatsapp/)
    """)
    image = Image.open('C:\streamlit\photo\whatsapp.jpg')
    st.image(image, caption='Gambar 3. Peretasan WA')

with tab4:
    st.header("Gimana agar Nggak Kena Hack?")
    st.video('https://www.youtube.com/watch?v=2WG9mvsl3Sw')

st.write("---")

option = st.sidebar.selectbox(
    'Silakan pilih:',
    ('Menu','Catfishing','Deepfake')
)

if option == 'Menu' or option == '':
    st.write("") #menampilkan halaman utama

elif option == 'Catfishing':
    #st.write("Catfishing adalah ketika seseorang membuat profil online palsu untuk mengelabui orang yang mencari cinta, biasanya untuk mendapatkan uang dari mereka. Dalam hal ini, pelaku menggunakan kata-kata yang memanipulasi, membujuk, dan mengeksploitasi agar permintaan dari pelaku nanti tidak menimbulkan kecurigaan.") #menampilkan judul halaman dataframe
    original_title = '<p style="font-family:Papyrus; color:Blue; font-size: 20px;">Catfishing merupakan kasus penipuan yang terjadi di dunia maya dengan berpura-pura menunjukkan ketertarikan kepada si korban, tapi untuk tujuan yang negatif. Misalnya, untuk merampok, memerkosa, menculik, hingga membunuh.</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.video("https://youtu.be/QhmI0G7-8SQ")

elif option == 'Deepfake':
    #st.write("""## Data Pengguna""") #menampilkan judul halaman 
    original_title = '<p style="font-family:Papyrus; color:Blue; font-size: 20px;">Deepfake adalah istilah yang digunakan secara umum untuk merujuk pada video apa pun di mana wajah telah ditukar atau diubah secara digital dengan bantuan kecerdasan buatan (AI).</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.video("https://youtu.be/LwfJWELSsjg")
    st.video("https://youtu.be/jxq5Yuy5vPg")


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