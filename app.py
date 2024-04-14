import streamlit as st

st.title("Streamlit demo app for loan status prediction")
st.header("This is the header line ")
st.subheader("This is the subheader line ")
st.text("This is the random text line")
st.success("Success")
st.warning("Warning")
st.info("information")
st.error("Error")

if st.checkbox("select/un-select"):
    st.text("user selcted checkbox ")
else:
    st.text("user unselcted checkbox ")

state = st.radio("what is your favorite color?",("Red",'Green','Yellow'))

if state == "Red":
    st.success("You have selected Red")

occupation = st.selectbox("what is your occupation?",['select here','student','Engineer','vlogger'])
st.text(f"selected option is {occupation}")

if st.button("Example Button"):
    st.error("you have clicked the button")

st.sidebar.header("Heading of sidebar")
st.sidebar.text("Created by Himanshu Choudhary")