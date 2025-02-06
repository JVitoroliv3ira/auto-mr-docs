from os import getenv

class Config:
    GITLAB_API_URL = getenv('GITLAB_API_URL')
    PROJECT_ID = getenv('CI_PROJECT_ID')
    MR_ID = getenv('CI_MERGE_REQUEST_IID')
    GITLAB_TOKEN = getenv('GITLAB_TOKEN')
    DEEPSEEK_API_KEY = getenv('DEEPSEEK_API_KEY')
    DEBUG = getenv('DEBUG', "False")
    
    REQUIRED_VARS = ["GITLAB_API_URL", "PROJECT_ID", "MR_ID", "GITLAB_TOKEN", "DEEPSEEK_API_KEY"]
    
    for var in REQUIRED_VARS:
        if not locals()[var]:
            raise ValueError(f"Erro: A variável de ambiente '{var}' não está definida.")
