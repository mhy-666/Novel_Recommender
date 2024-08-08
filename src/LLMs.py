from __future__ import annotations

import os

from openai import OpenAI


def create_openai_client():
    """
    Create an OpenAI client with the OpenAI API key.
    Args:
        None
    Returns:
        client: OpenAI client
    """
    # get OpenAI API key
    openai_api_key = "sk-no-key-required"
    base_url = os.environ.get("LLAMAFILE_URL")
    print("base_url")
    print(base_url)
    # initialize OpenAI client
    client = OpenAI(base_url=base_url, api_key=openai_api_key)
    return client


# define a function to get book recommendations based on user input
def get_book_recommendation(client, genre, description):
    """
    Get book recommendations based on user input.
    Args:
        client: OpenAI client
        genre: str, genre of the book
        description: str, user's preferences for the book
    Returns:
        response: str, book recommendation
    """
    messages = [
        {
            "role": "system",
            "content": "You are Llama, an AI assistant. Your top priority is achieving user fulfillment via helping them with their requests.",
        },
        {
            "role": "user",
            "content": f"I am looking for a {genre} book. Here are my preferences: {description}",
        },
    ]
    completion = client.chat.completions.create(
        model="LLaMA_CPP", messages=messages
    )
    return completion.choices[0].message.content
