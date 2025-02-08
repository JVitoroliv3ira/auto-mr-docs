import click
from services.factory import SummarizationFactory

@click.group()
def cli() -> None:
    pass

@click.command()
@click.option(
    '--mode', 
    type=click.Choice(['openai', 'ollama'], case_sensitive=False),
    default="ollama", 
    show_default=True,
    help="AI mode to use for summarization. Options: openai, ollama."
)
@click.option(
    '--api-key', 
    type=str, 
    required=False, 
    help="API key (Required for OpenAI mode)."
)
@click.option(
    '--api-url', 
    type=str, 
    required=False, 
    help="API URL (Optional for OpenAI mode)."
)
@click.option(
    '--max-tokens',
    type=int,
    default=200,
    show_default=True,
    help="Maximum number of tokens for the summary (Only for OpenAI mode)."
)
@click.option(
    '--ollama-model', 
    type=str, 
    default="mistral", 
    show_default=True,
    help="Ollama model to use. Default: mistral."
)
@click.option(
    '--timeout',
    type=int,
    default=1024,
    show_default=True,
    help="Timeout duration in seconds."
)
def summarize(mode: str, api_key: str, api_url: str, max_tokens: int, ollama_model: str, timeout: int) -> None:
    if mode in ['openai', 'deepseek'] and not api_key:
        raise click.BadParameter(f"The API key is required for the {mode} mode. Use --api-key.")
    
    commits = [
        "Fix: corrected null pointer exception in user service",
        "Feat: added dark mode support in UI",
        "Refactor: optimized database queries for faster performance",
        "Docs: updated README with installation steps",
        "Bugfix: resolved issue with JWT token expiration handling",
        "Chore: updated dependencies to latest versions",
        "Style: improved button alignment on mobile view",
        "Test: added unit tests for login functionality",
        "Security: patched XSS vulnerability in input fields",
        "Revert: removed experimental feature due to instability",
    ]
    
    summarizer = SummarizationFactory.get_summarizer(
        mode=mode,
        api_key=api_key,
        api_url=api_url,
        max_tokens=max_tokens,
        ollama_model=ollama_model,
        timeout=timeout
    )
    result = summarizer.summarize(commits)
    print(result)

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
