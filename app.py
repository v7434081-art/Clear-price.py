import streamlit as st

st.title("Registration Form")

with st.form("registration_form"):

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    age = st.number_input("Age", min_value=1, max_value=100, step=1)

    gender = st.radio("Gender", ["Male", "Female", "Other"])

    city = st.selectbox(
        "City",
        ["Select City", "Delhi", "Chandigarh", "Amritsar", "Kangra"]
    )

    agree = st.checkbox("I agree to the terms and conditions")

    submit = st.form_submit_button("Register")

    if submit:
        if name == "":
            st.error("Please enter your name")

        elif email == "":
            st.error("Please enter your email")

        elif password == "":
            st.error("Please enter your password")

        elif city == "Select City":
            st.error("Please select your city")

        elif not agree:
            st.error("Please agree to the terms and conditions")

        else:
            st.success("Registration Successful! 🎉")
            st.write("Name:", name)
            st.write("Email:", email)
            st.write("Age:", age)
            st.write("Gender:", gender)
            st.write("City:", city)
