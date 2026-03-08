from dotenv import load_dotenv
import os

load_dotenv()

def get_model_name():
    
    """Loading OpenAI Model From .env file"""
    
    model_name = os.getenv("OPENAI_MODEL")
    
    if model_name:
        return model_name
    
    else:
        raise "Model with Key Name 'OPENAI_MODEL' Not Found in .env"


def get_api_key():
    
    """Loading OpenAI APi Key From .env file"""
    
    api_key = os.getenv("OPENAI_API_KEY")
    
    if api_key:
        return api_key
    
    else:
        raise "API Key with Key Name 'OPENAI_API_KEY' Not Found in .env"


def get_base_url():
    
    """Loading OpenAI APi Key From .env file"""
    
    base_url = os.getenv("OPENAI_BASE_URL")
    
    if base_url:
        return base_url
    
    else:
        raise "Base URL Key with Key Name 'OPENAI_BASE_URL' Not Found in .env"


