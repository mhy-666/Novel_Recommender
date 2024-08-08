import unittest
from unittest.mock import patch, MagicMock
from src.LLMs import create_openai_client, get_book_recommendation 

class TestOpenAIClient(unittest.TestCase):

    @patch('src.LLMs.OpenAI') 
    @patch('os.environ.get')
    def test_create_openai_client(self, mock_env_get, MockOpenAI):
        # Set up mock environment variable and OpenAI client
        mock_env_get.return_value = 'https://localhost'
        mock_openai_instance = MagicMock()
        MockOpenAI.return_value = mock_openai_instance

        # Call the function
        client = create_openai_client()

        # Assert that OpenAI client is initialized correctly
        MockOpenAI.assert_called_once_with(
            base_url='https://localhost',
            api_key='sk-no-key-required'
        )
        self.assertEqual(client, mock_openai_instance)

    @patch('src.LLMs.OpenAI')
    def test_get_book_recommendation(self, MockOpenAI):
        # Set up mock OpenAI client
        mock_openai_instance = MagicMock()
        MockOpenAI.return_value = mock_openai_instance

        # Set up mock completion response
        mock_completion = MagicMock()
        mock_completion.choices[0].message.content = "Recommended Book Title"
        mock_openai_instance.chat.completions.create.return_value = mock_completion

        # Create client and call the function
        client = create_openai_client()
        result = get_book_recommendation(client, 'science fiction', 'space travel and adventure')

        # Assert that the completion method was called correctly
        mock_openai_instance.chat.completions.create.assert_called_once_with(
            model="LLaMA_CPP",
            messages=[
                {"role": "system", "content": "You are Llama, an AI assistant. Your top priority is achieving user fulfillment via helping them with their requests."},
                {"role": "user", "content": "I am looking for a science fiction book. Here are my preferences: space travel and adventure"}
            ]
        )
        # Assert that the function returns the expected result
        self.assertEqual(result, "Recommended Book Title")

if __name__ == '__main__':
    unittest.main()
