import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Birthday to Saithi",
    page_icon="🎉",  # You can use an emoji or a path to an image file
    layout="wide"
)

# Your Streamlit app code here
st.title("Happy BirthDay to Saithi ! 🎉")
st.write("Let's celebrate with some best pics!")


col1,col2= st.columns(2,gap="large")
col1.image("Saithi1.jpg")
col2.image("Saithi2.png")







