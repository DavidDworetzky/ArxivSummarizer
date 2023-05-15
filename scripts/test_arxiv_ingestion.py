import json 
import requests

def test_ingestion():
    """
    Test ingestion of articles
    """
    #load articles from resources / arxiv_presets.json
    with open('resources/arxiv_presets.json') as f:
        data = json.load(f)


#if main
#execute script
if __name__ == "__main__":
    test_ingestion()