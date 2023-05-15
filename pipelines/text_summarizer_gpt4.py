from pipelines.text_summarizer import TextSummarizer
from pipelines.text_summarizer_constants import SUMMARIZER_PROMPT
from typing import Any
import requests
import openai 
#class that implements text summarizer
class TextSummarizerGPT4(TextSummarizer):
    def __init__(self, api_key):
        self.api_key = api_key

    def summarize(self, text) -> str:
        """
        Summarize the given text
        :param text: text to summarize
        :return: summary of the text
        """

        #call to openai api to summarize the text
        #create the prompt
        prompt = SUMMARIZER_PROMPT + "\n\n" + text + "\n\n"
        #create the parameters
        params = {
            "prompt": prompt,
            "max_tokens": 100,
            "temperature": 0.7,
            "top_p": 1,
            "frequency_penalty": 0.5,
            "presence_penalty": 0.5,
            "stop": ["\n\n"]
        }
        #make the request
        response = requests.post("https://api.openai.com/v1/engines/davinci-codex/completions", json=params, headers={"Authorization": "Bearer " + self.api_key})

        if response.status_code == 200:
            return response.json()
        
    def generate_embedding(self, text) -> str:
        """
        Generate an embedding for the given text
        :param text: text to generate embedding for
        :return: embedding of the text
        """
        # Call the OpenAI API to generate an embedding for the input text
        response = openai.Completion.create(
            engine="text-embedding-ada-002",
            prompt=text,
            n=1,
            max_tokens=1,
            temperature=0.7,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
    
        # Extract the embedding from the API response
        embedding = response.choices[0].text.strip()
        return embedding





