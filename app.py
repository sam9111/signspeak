import streamlit as st


# Define the main function for the multipage app
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a page:", ["Home", "About", "Contact"])

    if page == "Home":
        home()
    elif page == "About":
        about()
    elif page == "Contact":
        contact()


def home():
    st.title("Home Page")
    st.write("Welcome to the Home page!")


def about():
    st.title("About Page")
    st.write("This is the About page.")


def contact():
    st.title("Contact Page")
    st.write("This is the Contact page.")


if __name__ == "__main__":
    main()
