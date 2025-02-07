from typing import List, Optional
from abc import ABC, abstractmethod

class Summarization(ABC):
    @abstractmethod
    def __init__(self, api_key: Optional[str] = None, api_url: Optional[str] = None, ollama_model: Optional[str] = "mistral"):
        self.api_key = api_key
        self.api_url = api_url
        self.ollama_model = ollama_model
    
    @abstractmethod
    def summarize(self, commits: List[str]) -> str:
        raise NotImplemented()