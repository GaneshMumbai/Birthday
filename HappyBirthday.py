import streamlit as st
import time

# Set the page configuration


st.set_page_config(
    page_title="Birthday to Saithi",
    page_icon="🎉",  # You can use an emoji or a path to an image file
    layout="wide",

)

# Your Streamlit app code here

st.markdown(
    """
    <style>
    .centered-blue-text {
        color: blue;
        font-size: 80px;
        font-weight: bold;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="centered-blue-text">Happy BirthDay to Saithi ! 🎉</h1>', unsafe_allow_html=True)

#st.title(":blue[Happy BirthDay to Saithi ! 🎉]")
st.divider()
#st.title(":red[Let's celebrate with some best pics!]")

st.markdown(
    """
    <style>
    .dark-pink-text {
        color: #e75480;  /* Dark pink color */
        font-size: 40px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="dark-pink-text">Let\'s celebrate with some best pics!</h1>', unsafe_allow_html=True)

col1,col2,col3,col4= st.columns(4)

col1.image("Saithi1.jpg")
col2.image("Saithi5.png")
col3.image("Saithi7.png")
col4.image("Saithi2.png")

st.divider()
st.header(":blue[May this year bring you endless happiness, new adventures, and countless opportunities to shine. Always remember that you are loved beyond measure, and I will always be here to support you in every step of your journey.]")

#st.title(":ornge[Enjoy your special day to the fullest! 🎉🎂🎁]")

st.markdown(
    """
    <style>
    .brown-text {
        color: brown;
        font-size: 60px;
        font-weight: bold;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="brown-text">Enjoy your special day to the fullest! 🎉🎂🎁</h1>', unsafe_allow_html=True)


for i in range(0,100):
    st.balloons()
    time.sleep(2)









