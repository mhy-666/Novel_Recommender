from __future__ import annotations

from data_processing import retrieve_recommendations
from data_processing import set_up_pinecone
from LLMs import create_openai_client


def get_book_recommendation_rag(client, genre, description):
    """
    Get book recommendations based on user input with rag
    Args:
        client: OpenAI client
        genre: str, genre of the book
        description: str, user's preferences for the book
    Returns:
        response: str, book recommendation
    """
    vector_store = set_up_pinecone(
        index_name="novels", namespace="novelvector"
    )
    query = retrieve_recommendations(vector_store, genre, k=1)
    context = "Here are some book recommendations for preferences:" + query
    messages = [
        {
            "role": "system",
            "content": "You are Llama, an AI assistant. Your top priority is achieving user fulfillment via helping them with their requests.",
        },
        {
            "role": "user",
            "content": f"I am looking for a {genre} book. Here are my preferences: {description}",
            "role": "assistant",
            "content": context,
        },
    ]
    completion = client.chat.completions.create(
        model="LLaMA_CPP", messages=messages
    )
    return completion.choices[0].message.content


if __name__ == "__main__":
    client = create_openai_client()
    result = get_book_recommendation_rag(
        client, "fantasy", "space travel and adventure"
    )
    print(result)
