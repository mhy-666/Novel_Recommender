from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
import os
from pinecone import Pinecone



def load_data(file_path):
    loader = CSVLoader(file_path=file_path)
    data = loader.load()
    return data


def split_text(data):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, add_start_index=True
    )
    all_splits = text_splitter.split_documents(data)
    return all_splits

def set_up_pinecone(index_name = 'novels', namespace = 'novelvector'):

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
    results = vector_store.similarity_search_with_score(query, k=k)
    return results