import streamlit as st
from openai import OpenAI

openai_api_key = 'sk-no-key-required'
# initialize OpenAI client
client = OpenAI(
    base_url="http://127.0.0.1:8080/v1",
    api_key=openai_api_key
)

# define a function to get book recommendations based on user input
def get_book_recommendation(genre, description):
    messages = [
        {"role": "system", "content": "You are Llama, an AI assistant. Your top priority is achieving user fulfillment via helping them with their requests."},
        {"role": "user", "content": f"I am looking for a {genre} book. Here are my preferences: {description}"}
    ]
    completion = client.chat.completions.create(
        model="LLaMA_CPP",
        messages=messages
    )
    return completion.choices[0].message.content

def main():
    st.title("Novel Recommendation System")

    # create a select box to allow users to
    genre = st.selectbox(
        "Select the genre you want to read:",
        ["Fantasy", "Science Fiction", "Mystery", "Romance", "Horror"]
    )

    # create a text area for users to describe their preferences
    description = st.text_area("Describe your preferences in more detail:")

    # create a button to get recommendations
    if st.button("Get Recommendation"):
        if genre and description:
            recommendation = get_book_recommendation(genre, description)
            st.write("Recommended Book:")
            st.write(recommendation)
        else:
            st.write("Please select a genre and provide a description.")

if __name__ == "__main__":
    main()
