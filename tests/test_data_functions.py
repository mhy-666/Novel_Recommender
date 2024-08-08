import pytest
from unittest.mock import MagicMock, patch
from src.data_processing import load_data, split_text, set_up_pinecone
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
import os
from pinecone import Pinecone

# Mock CSVLoader
class MockCSVLoader:
    def __init__(self, file_path):
        pass
    
    def load(self):
        return ["document1", "document2"]

# Mock Pinecone
class MockPinecone:
    def __init__(self, api_key):
        pass
    
    class Index:
        def __init__(self, index_name):
            pass
        
        def describe_index_stats(self):
            pass

# Test load_data
@patch('..src.data_processing.CSVLoader', new_callable=MockCSVLoader)
def test_load_data(mock_loader):
    result = load_data("dummy_path")
    assert result == ["document1", "document2"]

# Test split_text
def test_split_text():
    mock_data = ["document1", "document2"]
    result = split_text(mock_data)
    assert isinstance(result, list)  # Check if result is a list

# Test set_up_pinecone
@patch('..src.data_processing.Pinecone', new_callable=MockPinecone)
@patch('..src.data_processing.HuggingFaceEmbeddings', return_value=MagicMock())
def test_set_up_pinecone(mock_embeddings, mock_pinecone):
    vector_store = set_up_pinecone()
    assert isinstance(vector_store, PineconeVectorStore)

if __name__ == "__main__":
    pytest.main()
