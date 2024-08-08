import unittest
from unittest.mock import patch, MagicMock
from src.data_processing import load_data, split_text, set_up_pinecone, retrieve_recommendations

class TestNovelRecommender(unittest.TestCase):

    @patch('src.data_processing.CSVLoader')
    def test_load_data(self, MockCSVLoader):
        # Arrange
        mock_loader_instance = MockCSVLoader.return_value
        mock_loader_instance.load.return_value = 'mocked_data'
        file_path = 'dummy_path.csv'

        # Act
        result = load_data(file_path)

        # Assert
        MockCSVLoader.assert_called_once_with(file_path=file_path)
        mock_loader_instance.load.assert_called_once()
        self.assertEqual(result, 'mocked_data')

    @patch('src.data_processing.RecursiveCharacterTextSplitter')
    def test_split_text(self, MockTextSplitter):
        # Arrange
        mock_splitter_instance = MockTextSplitter.return_value
        mock_splitter_instance.split_documents.return_value = 'split_data'
        data = 'mocked_data'

        # Act
        result = split_text(data)

        # Assert
        MockTextSplitter.assert_called_once_with(chunk_size=1000, chunk_overlap=200, add_start_index=True)
        mock_splitter_instance.split_documents.assert_called_once_with(data)
        self.assertEqual(result, 'split_data')


    @patch('src.data_processing.PineconeVectorStore')
    def test_retrieve_recommendations(self, MockVectorStore):
        # Arrange
        mock_vector_store_instance = MockVectorStore.return_value
        mock_vector_store_instance.similarity_search_with_score.return_value = 'mock_results'
        query = 'find me a book'
        k = 1

        # Act
        result = retrieve_recommendations(mock_vector_store_instance, query, k)

        # Assert
        mock_vector_store_instance.similarity_search_with_score.assert_called_once_with(query, k=k)
        self.assertEqual(result, 'mock_results')

if __name__ == '__main__':
    unittest.main()
