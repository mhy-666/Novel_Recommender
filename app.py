import streamlit as st
from openai import OpenAI
import os
from src.LLMs import get_book_recommendation, create_openai_client


def main():
    st.title("Novel Recommendation System")

    # create a select box to allow users to
    genre = st.selectbox(
        "Select the genre you want to read:",
        ["Fantasy", "Science Fiction", "Mystery", "Romance", "Horror"]
    )

    # create a text area for users to describe their preferences
    description = st.text_area("Describe your preferences in more detail:")

    # create an OpenAI client
    client = create_openai_client()


    # create a button to get recommendations
    if st.button("Get Recommendation"):
        if genre and description:
            recommendation = get_book_recommendation(client, genre, description)
            st.write("Recommended Book:")
            st.write(recommendation)
        else:
            st.write("Please select a genre and provide a description.")

if __name__ == "__main__":
    main()
