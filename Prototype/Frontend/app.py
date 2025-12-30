import streamlit as st
import requests
st.set_page_config(
    page_title="EasyWay-Expense Tracker For Indian Students",
    layout="centered"
)
st.title("EasyWay\n Tracker For Indian Students")
st.write("Upload bill/UPI screenshots or enter expense text.")
options=st.radio("Choose input method:",["Text","Image"])
if options=="Text":
    text_input=st.text_input("enter your expense details",placeholder="paid \u20B9250 to zomato via UPI")
elif options=="Image":
    image_input=st.file_uploader("upload UPI screenshot or Bill")
    if image_input:
        st.image(image_input,caption="Uploaded Image",use_column_width=True)
if st.button("Extract Expense"):
    if options == "Text" and text_input:
        # Demo output without backend
        demo_json = {
            "amount": 250,
            "category": "Food",
            "merchant": "Zomato",
            "date": "2025-12-25",
            "payment_mode": "UPI",
            "confidence": 0.95,
            "reasoning": "Demo output"
        }
        st.subheader("Extracted Expense (Demo)")
        st.json(demo_json)


    else:
        st.warning("Please enter expense text")
