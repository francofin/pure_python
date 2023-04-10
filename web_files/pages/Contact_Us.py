import streamlit as st
# from pages.my_web_utils.web_functions import add_bg_from_local
# from pages.my_web_utils.send_emails import send_an_email

# add_bg_from_local("images/bg1.jpg")
st.header(":green[Contact Us]")


with st.form(key="user_email_form"):
    user_email = st.text_input("Please Enter Your Email Address")
    username = "francoiskieran89@gmail.com"
    user_message = st.text_area("Enter Your Email")
    message = f"""
        From:{user_email}
        Subject: New email fro {user_email}
    
        {user_message}
    """

    submitted = st.form_submit_button("Submit")
#     The submit button returns a boolean.
    if submitted:
        send_an_email(message)
        st.success("Email succesfully delivered")
