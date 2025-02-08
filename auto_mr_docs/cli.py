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
    help="AI mode to use for summarization (openai, ollama)."
)
@click.option(
    '--api-key', 
    type=str, 
    required=False, 
    help="API key (required for openai mode)."
)
@click.option(
    '--api-url', 
    type=str, 
    required=False, 
    help="API URL (optional for openai mode)."
)
@click.option(
    '--ollama-model', 
    type=str, 
    default="mistral", 
    show_default=True,
    help="Ollama model to use (default: mistral)."
)
def summarize(mode: str, api_key: str, api_url: str, ollama_model: str) -> None:
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
    
    summarizer = SummarizationFactory.get_summarizer(mode=mode, api_key=api_key, api_url=api_url, ollama_model=ollama_model)
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
