from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_tracing_disabled,
    OpenAIChatCompletionsModel,
)
from ai_agent.my_secrets import Secrets
from rich import print

secrets = Secrets()


external_client = AsyncOpenAI(
    base_url=secrets.gemini_api_url,
    api_key=secrets.gemini_api_key,
)

set_tracing_disabled(True)


agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant. Which can precisely answer questions in a single sentence.",
    model=OpenAIChatCompletionsModel(
        openai_client=external_client,
        model=secrets.gemini_api_model,
    ),
)


def main() -> None:

    prompt = "What is GenAI?"

    result = Runner.run_sync(
        starting_agent=agent,
        input=prompt,
    )

    print(f"\n[green]Prompt:[/green] {prompt}\n")
    print(f"[green]Response:[/green] {result.final_output}\n")
