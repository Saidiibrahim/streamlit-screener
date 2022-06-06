# Import Streamlit
import streamlit as st


# Declare a form and call methods directly on the returned object
def config_page():
    # Declare a form and call methods directly on the returned object
    form = st.form(key='my_form')
    api_key = form.text_input(label='Enter some text')
    submit_button = form.form_submit_button(label='Submit')


st.set_page_config(page_title="API Setup", page_icon="🚀")
st.markdown("# API Setup")
st.sidebar.header("Plotting Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)
config_page()

