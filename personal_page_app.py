import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pyttsx3 as sp
from PIL import Image





st.set_page_config(
    page_title="My Digital Profile", page_icon=":tada:", layout="wide"
)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

lottie_coding=load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_8kut1rsr.json")

# Header Section 
with st.container():
    st.subheader("Hi, I am Rafik :wave:")
    st.title("A Software Engineer From Maryland, USA")
    st.write("I am passionate about coding, music, outdoor adventures, camping, and hiking...")
    #sp.speak("Hi, I am Rafik. A Software Engineer From USA.I am passionate about coding, fishing, and music. What about you? ")


with st.container():
    st.write("---")
    left_col, right_col = st.columns(2)
    with left_col:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I currently work as a Solutions Architect at CareFirst BCBS. I have built and contributed to many technology projects in the areas of:
            - Test and QA automation
            - DevOps and infrastructre automation
            - Performance engineering and APM
            - Machine Learning and Natural Language Processing NLP using Python
            - Open source technologies
            [Visit my Linkedin Profile](https://www.linkedin.com/in/rkouissar/)
            """
        )

with right_col:
    #st_lottie(lottie_coding, height=300, key="coding")
    image = Image.open('assets/me.jpg')
    st.image(image, caption='Sunshine by the island',  clamp=False)


# 
# with st.container():


# ---- PROJECTS ----
# with st.container():
#     st.write("---")
#     st.header("My Projects")
#     st.write("##")
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#         st.image(img_lottie_animation)
#     with text_column:
#         st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
#         st.write(
#             """
#             Learn how to use Lottie Files in Streamlit!
#             Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
#             In this tutorial, I'll show you exactly how to do it
#             """
#         )
#         st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
# with st.container():
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#         st.image(img_contact_form)
#     with text_column:
#         st.subheader("How To Add A Contact Form To Your Streamlit App")
#         st.write(
#             """
#             Want to add a contact form to your Streamlit website?
#             In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
#             """
#         )
#         st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/kouissar@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with right_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with left_column:
        # st.empty()
        st_lottie(
            lottie_coding,
            speed=1,
            reverse=False,
            loop=True,
            quality="low", #medium, high
            # renderer="svg", #canvas
            height="None",
            width="None",
            key="None",


        )