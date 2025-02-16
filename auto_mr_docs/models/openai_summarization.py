import openai

from typing import List, Optional
from auto_mr_docs.config.config import get_prompt
from auto_mr_docs.config.logger import LoggerConfig
from auto_mr_docs.models.base import Summarization

logger = LoggerConfig.get_logger()

class OpenAISummarization(Summarization):
    def __init__(self, api_key: str, api_url: Optional[str] = None, max_tokens: Optional[int] = 200, timeout: Optional[int] = 1024):
        super().__init__(api_key=api_key, api_url=api_url, max_tokens=max_tokens, timeout=timeout)
        logger.info(f"OpenAISummarization initialized.")
        self.client = openai.OpenAI(api_key=api_key, base_url=api_url) if api_url else openai.OpenAI(api_key=api_key)
    
    def summarize(self, commits: List[str]) -> str:
        if not commits:
            logger.error("Commit list is empty. Summarization requires at least one commit.")
            return "Error: No commits provided."

        logger.info(f"Starting summarization for {len(commits)} commits.")
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": get_prompt(commits)}
                ],
                max_completion_tokens=self.max_tokens,
                timeout=self.timeout,
            )
            
            prompt_tokens = response.usage.prompt_tokens
            completion_tokens = response.usage.completion_tokens
            total_tokens = response.usage.total_tokens
            logger.info(f"Token usage - Prompt: {prompt_tokens}, Completion: {completion_tokens}, Total: {total_tokens}")

            summary = response.choices[0].message.content.strip()
            return summary
        except Exception as e:
            logger.error(f"Error during summarization: {str(e)}")
            return "Error: Failed to generate summary."
