import requests
from typing import List

from config import Config
from logger import LoggerConfig

logger = LoggerConfig.get_logger()

class DeepSeekAPI:
    
    API_URL = Config.DEEPSEEK_API_URL
    API_KEY = Config.DEEPSEEK_API_KEY
    
    @staticmethod
    def generate_description_by_commits(commits: List[str]) -> str:
        
        if not commits:
            logger.warning('Nenhum commit foi passado para geração da descrição.')
            return "Nenhuma descrição disponível."
        
        prompt = "Resuma detalhadamente os seguintes commits e gere uma descrição clara e profissional para um Merge Request:\n\n"
        prompt += "\n".join(commits)
        
        payload = {
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": prompt}]
        }
        
        headers = {
            "Authorization": f"Bearer {Config.DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(DeepSeekAPI.API_URL, json=payload, headers=headers)
            response.raise_for_status()
            description = response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
            
            if not description:
                logger.warning("DeepSeek retornou uma resposta vazia.")
                return "Erro ao gerar descrição automática."
            
            return description.strip()
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao conectar à API do DeepSeek: {e}")
            return "Erro ao gerar descrição automática."
