from config import Config
from logger import LoggerConfig

def main() -> None:
    logger = LoggerConfig.get_logger()
    
    try:
        logger.info("Iniciando auto-mr-docs... 🚀")
        logger.info(f"GITLAB_API_URL: {Config.GITLAB_API_URL}")
        logger.info(f"PROJECT_ID: {Config.PROJECT_ID}")
        logger.info(f"MR_ID: {Config.MR_ID}")
        logger.info(f"GITLAB_TOKEN: {'***' if Config.GITLAB_TOKEN else 'NÃO DEFINIDO'}")
        logger.info(f"DEEPSEEK_API_KEY: {'***' if Config.DEEPSEEK_API_KEY else 'NÃO DEFINIDO'}")

        logger.info("Configurações carregadas com sucesso! ✅")

    except ValueError as e:
        logger.error(f"Erro crítico na configuração: {e}")

if __name__ == '__main__':
    main()
