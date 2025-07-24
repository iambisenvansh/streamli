import streamlit as st 

st.title("Chai Maker App")

if st.button("Make chai"):
    st.success("Your chai is being brewed")
    
add_masala= st.checkbox("Add Masala")

if add_masala:
    st.write("Masala added to your chai")

chai_base = st.radio("Pick your chai base: ", ["Milk", "Water", "Honey"])
st.write(f"Selected base for chai: {chai_base}")

flavours = st.selectbox("Choose flavour: ", ["Adrak","kesar", "Tulsi"])
st.write(f"Selected Flavour: {flavours}")

sugar = st.slider("Sugar level: ", 0, 5, 4)

cups = st.number_input("Number of cups: ", min_value= 1, max_value=10, step =1)
st.write(f"Selected Flavour: {cups}")

name = st.text_input("Enter your name")
if name:
    st.write(f"Welcome , {name} ! Your chai is on the way")
    
dob = st.date_input("Select your date of birth") 
st.write(f"Your date of birth {dob}")   