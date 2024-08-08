from openai import OpenAI
import os

def get_book_recommendation_with_rag(client, genre, description):
    '''
    Get book recommendations based on user input with rag
    Args:
        client: OpenAI client
        genre: str, genre of the book
        description: str, user's preferences for the book
    Returns:
        response: str, book recommendation
    '''
    messages = [
        {"role": "system", "content": "You are Llama, an AI assistant. Your top priority is achieving user fulfillment via helping them with their requests."},
        {"role": "user", "content": f"I am looking for a {genre} book. Here are my preferences: {description}"}
    ]
    completion = client.chat.completions.create(
        model="LLaMA_CPP",
        messages=messages
    )
    return completion.choices[0].message.content