import streamlit as st 
from PIL import Image

 
st.set_page_config(
    page_title="Profil Penulis",
    page_icon="🚣🏽‍♀️",
    layout="wide"
)
st.snow()

st.sidebar.success("Ini adalah halaman yang memuat informasi pembuat website dan penulis.")

with st.container():
    original_title = '<p style="font-family:Fantasy; color:Purple; font-size: 30px;">Authors (Gebetania)</p>'
    st.markdown(original_title, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    st.markdown("<h5 style='text-align: center; color: grey;'>Pricillia Astrid Dwi Saputri</h5>", unsafe_allow_html=True)
    image = Image.open('C:\streamlit\photo\pricillia.jpeg')
    st.image(image, caption=None, width=200)
with col3:
    st.write(' ')
    (  "\n")


st.write("---")

st.header(":mailbox: Get In Touch With Us!")

contact_form = """
<form action="https://formsubmit.co/pricillia_astrid@yahoo.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Details of your problem">"Your message here"</textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

col1, col2 = st.columns(2)

with col1:
    st.header("")
    st.markdown("![Alt Text](https://www.animatedimages.org/data/media/523/animated-hello-image-0042.gif)")

with col2:
    st.header("")
    st.markdown("![Alt Text](https://www.animatedimages.org/data/media/521/animated-have-a-nice-day-image-0002.gif)")


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





    


