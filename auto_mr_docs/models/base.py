from typing import List, Optional
from abc import ABC, abstractmethod

class Summarization(ABC):
    @abstractmethod
    def __init__(
        self,
        api_key: Optional[str] = None,
        api_url: Optional[str] = None,
        max_tokens: Optional[int] = 200,
        ollama_model: Optional[str] = "mistral",
        timeout: Optional[int] = 1024
    ) -> None:
        self.api_key = api_key
        self.api_url = api_url
        self.max_tokens = max_tokens
        self.ollama_model = ollama_model
        self.timeout = timeout
    
    @abstractmethod
    def summarize(self, commits: List[str]) -> str:
        raise NotImplemented()