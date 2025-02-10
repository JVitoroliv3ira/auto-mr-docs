import sys
import click
from config.logger import LoggerConfig
from services.factory import SummarizationFactory
from services.gitlab_service import GitlabService

logger = LoggerConfig.get_logger()

@click.group()
def cli() -> None:
    pass

@click.command()
@click.option(
    '--mode',
    type=click.Choice(['openai', 'ollama'], case_sensitive=False),
    default="ollama",
    show_default=True,
    help="Sets the AI mode used for summarization. Accepts 'openai' or 'ollama'."
)
@click.option(
    '--gitlab-token',
    type=str,
    required=True,
    help="Specifies your GitLab personal access token."
)
@click.option(
    '--project-id',
    type=int,
    required=True,
    help="Specifies the GitLab project ID."
)
@click.option(
    '--mr-id',
    type=int,
    required=True,
    help="Specifies the Merge Request ID."
)
@click.option(
    '--api-key',
    type=str,
    required=False,
    help="Specifies the API key (required for OpenAI mode)."
)
@click.option(
    '--api-url',
    type=str,
    required=False,
    help="Specifies the API endpoint (optional for OpenAI mode)."
)
@click.option(
    '--ollama-model',
    type=str,
    default="mistral",
    show_default=True,
    help="Specifies the Ollama model to use."
)
@click.option(
    '--max-tokens',
    type=int,
    default=200,
    show_default=True,
    help="Sets the maximum number of tokens for the summary (only for OpenAI mode)."
)
@click.option(
    '--timeout',
    type=int,
    default=1024,
    show_default=True,
    help="Sets the timeout duration in seconds."
)
def summarize(
    mode: str,
    gitlab_token: str,
    project_id: int,
    mr_id: int,
    api_key: str,
    api_url: str,
    max_tokens: int,
    ollama_model: str,
    timeout: int
) -> None:
    if mode == 'openai' and not api_key:
        raise click.BadParameter(f"The API key is required for the {mode} mode. Use --api-key.")
    
    try:
        logger.info(f"Starting summarization for MR {mr_id} in project {project_id}...")
    
        gitlab_service = GitlabService(private_token=gitlab_token, project_id=project_id)
        commits = gitlab_service.get_merge_request_commits(mr_id=mr_id)
        logger.info(f"Retrieved {len(commits)} commits from MR {mr_id}.")
        
        if not commits:
            logger.warning(f"No commits found for MR {mr_id}.")
            return
        
        summarizer = SummarizationFactory.get_summarizer(
            mode=mode,
            api_key=api_key,
            api_url=api_url,
            max_tokens=max_tokens,
            ollama_model=ollama_model,
            timeout=timeout
        )
        
        result = summarizer.summarize(commits)
        logger.info("Summary generated successfully!")
        
        gitlab_service.update_merge_request_description(mr_id=mr_id, new_description=result)
        logger.info(f"MR {mr_id} description updated successfully.")
    except Exception as e:
        logger.error(f"Error during execution: {e}", exc_info=True)
        sys.exit(-1)


@click.command()
def help() -> None:
    click.echo("auto-mr-docs CLI for GitLab Merge Request Summarization")
    click.echo("\nUsage:")
    click.echo("  auto-mr-docs [command] [options]\n")
    click.echo("Available commands:")
    click.echo("  summarize    Summarize the commits of a Merge Request in GitLab")
    click.echo("  help         Show available commands and their descriptions")

cli.add_command(summarize)
cli.add_command(help)

if __name__ == '__main__':
    cli()
