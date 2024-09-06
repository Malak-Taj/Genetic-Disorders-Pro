import streamlit as st

# Title of the contact page
st.markdown("""
    <h1 style='text-align: left; color: lavender; font-family: Arial; font-size: 2em;'>Contact Me!</h1>
""", unsafe_allow_html=True)

# Introduction or message
st.markdown("""
If you have any questions, feedback, or inquiries, feel free to reach out me using the form below. I'd like to hear from you!
""")

# Contact Form
st.subheader("Get in Touch :")
name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")

# Submit button
if st.button("Submit"):
    if name and email and message:
        # Here you would normally handle the form submission
        # e.g., send an email or store the information in a database
        st.success("Thank you for your message! I'll get back to you soon.")
    else:
        st.error("Please fill out all fields before submitting.")

# Alternative contact information
st.subheader("Other Ways to Reach Me :")
st.markdown("""
- **Email**: malaktaj2002.com
- **Whats**: +249-996-908-444
""")

# Social media links (Optional)
st.subheader("Follow Me :")
st.markdown("""
- [LinkedIn](https://www.linkedin.com)
- [Twitter](https://twitter.com)
- [Facebook](https://www.facebook.com)
""")
