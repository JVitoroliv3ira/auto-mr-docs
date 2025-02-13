from typing import Optional, Dict, Type

from auto_mr_docs.models.base import Summarization
from auto_mr_docs.models.openai_summarization import OpenAISummarization
from auto_mr_docs.models.ollama_summarization import OllamaSummarization

class SummarizationFactory:
    _summarizers: Dict[str, Type[Summarization]] = {
        "openai": OpenAISummarization,
        "ollama": OllamaSummarization
    }
    
    @staticmethod
    def get_summarizer(
        mode: str,
        api_key: Optional[str] = None,
        api_url: Optional[str] = None,
        max_tokens: int = 200,
        ollama_model: str = "ministry",
        timeout: int = 1024
    ) -> Summarization:
        mode = mode.lower()
        summarizer_cls = SummarizationFactory._summarizers.get(mode)
        
        if not summarizer_cls:
            raise ValueError(f"Invalid mode: {mode}. Choose from {list(SummarizationFactory._summarizers.keys())}.")
        
        if mode == "openai":
            return summarizer_cls(api_key=api_key, api_url=api_url, max_tokens=max_tokens, timeout=timeout)
        
        return summarizer_cls(ollama_model=ollama_model, timeout=timeout)
