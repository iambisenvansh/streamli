import streamlit as st 

st.title("Hello, Streamlit!")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first intreactive app")
st.write("Choose your fav. variety of coffee")

chai = st.selectbox("Your fav chai: ", ["Masala chai", 
                                        "lemon tea", " Adrak Chai", "Kesar Chai"])

st.write(f"Your choose {chai}. Excellent choice!")

st.success("Your chai has been brewed")