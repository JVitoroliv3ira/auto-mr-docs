from subprocess import run, CalledProcessError, TimeoutExpired
from typing import List

from models.base import Summarization
from config.logger import LoggerConfig
from config.config import get_prompt

logger = LoggerConfig.get_logger()

class OllamaSummarization(Summarization):
    def __init__(self, ollama_model: str = "mistral", timeout: int = 1024):
        super().__init__(ollama_model=ollama_model, timeout=timeout)
        logger.info(f"OllamaSummarization initialized with model: {ollama_model}")

    def summarize(self, commits: List[str]) -> str:
        if not commits:
            logger.error("Commit list is empty. Summarization requires at least one commit.")
            return "Error: No commits provided."

        logger.info(f"Starting summarization for {len(commits)} commits.")

        try:
            result = run(
                ["ollama", "run", self.ollama_model, get_prompt(commits)],
                capture_output=True,
                text=True,
                timeout=self.timeout
            )
            response = result.stdout.strip()

            if result.returncode != 0:
                logger.warning(f"Ollama process returned a non-zero exit code: {result.returncode}")
                return f"Error: Ollama process failed with code {result.returncode}."

            logger.info("Summarization completed successfully.")
            return response
        except TimeoutExpired:
            logger.error("Ollama summarization process timed out.")
            return "Error: Ollama process timed out."
        except CalledProcessError as e:
            logger.error(f"Ollama summarization failed with error: {e}")
            return f"Error: Ollama process failed with error {str(e)}"
        except Exception as e:
            logger.exception("An unexpected error occurred during summarization.")
            return f"Error: Unexpected issue - {str(e)}"
