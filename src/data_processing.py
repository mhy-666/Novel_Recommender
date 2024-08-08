from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
import os
from pinecone import Pinecone



def load_data(file_path):
    '''
    Load data from a CSV file.
    Args:
        file_path: str, path to the CSV file
    Returns:
        data: pandas DataFrame, data loaded from the CSV file
    '''
    loader = CSVLoader(file_path=file_path)
    data = loader.load()
    return data


def split_text(data):
    '''
    Split text data into chunks.
    Args:
        data: pandas DataFrame, data to be split
    Returns:
        all_splits: list, list of text chunks
    ''' 
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, add_start_index=True
    )
    all_splits = text_splitter.split_documents(data)
    return all_splits

def set_up_pinecone(index_name = 'novels', namespace = 'novelvector'):
    '''
    Set up Pinecone vector store.
    Args:
        index_name: str, name of the index
        namespace: str, namespace of the index
    Returns:
        vector_store: PineconeVectorStore, Pinecone vector store
    '''

    # initialize connection to pinecone (get API key at app.pinecone.io)
    api_key = os.environ.get('PINECONE_API_KEY')

    # configure client
    pc = Pinecone(api_key=api_key)

    index = pc.Index(index_name)
    # wait a moment for connection

    index.describe_index_stats()
    embeddings_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

    vector_store = PineconeVectorStore(index=index, namespace=namespace, embedding=embeddings_model)
    return vector_store

def retrieve_recommendations(vector_store, query, k=1):
    '''
    Retrieve recommendations from Pinecone vector store.
    Args:
        vector_store: PineconeVectorStore, Pinecone vector store
        query: str, query text
        k: int, number of recommendations to retrieve
    Returns:
        results: list, list of recommendations
    '''
    results = vector_store.similarity_search_with_score(query, k=k)
    return results