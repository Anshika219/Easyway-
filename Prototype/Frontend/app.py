import streamlit as st
import requests

# Backend URL
BACKEND_URL = "http://127.0.0.1:8000/parse-expense"

st.set_page_config(
    page_title="EasyWay - Expense Tracker For Indian Students",
    layout="centered"
)

st.title("EasyWay 💸")
st.subheader("Expense Tracker For Indian Students")
st.write("Upload bill/UPI screenshots or enter expense text.")

options = st.radio("Choose input method:", ["Text", "Image"])

text_input = None
image_input = None

if options == "Text":
    text_input = st.text_input(
        "Enter your expense details",
        placeholder="Paid ₹250 to Zomato via UPI"
    )

elif options == "Image":
    image_input = st.file_uploader(
        "Upload UPI screenshot or Bill",
        type=["png", "jpg", "jpeg"]
    )
    if image_input:
        st.image(image_input, caption="Uploaded Image", use_column_width=True)

# Button
if st.button("Extract Expense"):
    if not text_input and not image_input:
        st.warning("Please provide expense text or image.")
    else:
        with st.spinner("Extracting expense details..."):
            data = {}
            files = {}

            if text_input:
                data["text"] = text_input

            if image_input:
                files["file"] = (
                    image_input.name,
                    image_input,
                    image_input.type
                )

            try:
                response = requests.post(
                    BACKEND_URL,
                    data=data,
                    files=files,
                    timeout=60
                )

                if response.status_code == 200:
                    result = response.json()

                    st.subheader("📊 Extracted Expense")
                    st.json(result)

                    # Pretty output
                    st.markdown("### Details")
                    st.write("**Amount:** ₹", result.get("amount"))
                    st.write("**Merchant:**", result.get("merchant"))
                    st.write("**Category:**", result.get("category"))
                    st.write("**Date:**", result.get("date"))
                    st.write("**Payment Mode:**", result.get("payment_mode"))
                    st.write("**Confidence:**", result.get("confidence"))
                    st.caption("Reasoning: " + result.get("reasoning", ""))

                else:
                    st.error("Backend error")
                    st.text(response.text)

            except requests.exceptions.RequestException as e:
                st.error("Could not connect to backend")
                st.exception(e)
