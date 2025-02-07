from typing import Optional, Dict, Type

from models.base import Summarization
from models.openai_summarization import OpenAISummarization
from models.ollama_summarization import OllamaSummarization

class SummarizationFactory:
    _summarizers: Dict[str, Type[Summarization]] = {
        "openai": OpenAISummarization,
        "ollama": OllamaSummarization
    }
    
    @staticmethod
    def get_summarizer(mode: str, api_key: Optional[str] = None, api_url: Optional[str] = None, ollama_model: str = "ministry") -> Summarization:
        mode = mode.lower()
        summarizer_cls = SummarizationFactory._summarizers.get(mode)
        
        if not summarizer_cls:
            raise ValueError(f"Invalid mode: {mode}. Choose from {list(SummarizationFactory._summarizers.keys())}.")
        
        if mode in ["openai", "deepseek"]:
            return summarizer_cls(api_key=api_key, api_url=api_url)
        
        return summarizer_cls(ollama_model=ollama_model)
