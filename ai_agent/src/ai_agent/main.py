from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_tracing_disabled,
    OpenAIChatCompletionsModel,
)
from ai_agent.my_secrets import Secrets
from rich import print
import asyncio
from openai.types.responses import ResponseTextDeltaEvent


secrets = Secrets()


external_client = AsyncOpenAI(
    base_url=secrets.gemini_api_url,
    api_key=secrets.gemini_api_key,
)

set_tracing_disabled(True)


agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    model=OpenAIChatCompletionsModel(
        openai_client=external_client,
        model=secrets.gemini_api_model,
    ),
)


async def main() -> None:

    prompt = "Write an 1000 word essay on AI"

    result = Runner.run_streamed(
        starting_agent=agent,
        input=prompt,
    )
    
    async for chunk in result.stream_events():
        if chunk.type =="raw_response_event" and isinstance(chunk.data, ResponseTextDeltaEvent):
            print(chunk.data.delta, end="", flush=True)


def run():
    asyncio.run(main())