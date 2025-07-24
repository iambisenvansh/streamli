import streamlit as st 

st.title("Chai Taste Poll")

col1, col2 = st.columns(2) 

with col1:
    st.header("Masala Chai")
    st.image("https://media.istockphoto.com/id/614533094/photo/indian-masala-chai-tea.jpg?s=612x612&w=0&k=20&c=0P-npS30JIBX0FA9csLyB0WYtkEU7gWkNE7nSnvXlSE=", width= 200)
    vote1 = st.button("Vote Masala Chai")
    
with col2:
    st.header("Adrak Chai")
    st.image("https://swachhtea.com/cdn/shop/files/1_13f36ba5-a4bd-47bd-b588-484f0ac3cbbf_1080x.jpg?v=1719233375", width = 200)
    vote2 = st.button("Vote Adrak Chai")

if vote1:
    st.success("Thanks for voting for Masala Chai!")
elif vote2:     
    st.success("Thanks for voting for Adrak Chai!")

name = st.sidebar.text_input("Enter your Name")
tea = st.sidebar.selectbox("Select your favourite tea", ["Masala Chai", "Adrak Chai", "Kesar Chai"])

st.write(f"Welcome {name} and your {tea} chai is getting ready")

with st.expander("Show Chai Making Instructions"):
    st.write("""
             1. Boil water with tea leaves
             2. Add spices like ginger or cardamon
             3. Serve hot with milk or sugar
             """)
st.markdown('### Welcome to the Chai Taste Poll!')
st.markdown('>Blockquote ')
    