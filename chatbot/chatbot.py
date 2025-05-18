import chainlit as cl
from rich import print
from my_secrets import Secrets
from agents import Agent, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled, Runner


@cl.on_message
async def main(msg: cl.Message):
    secrets = Secrets()
    external_client = AsyncOpenAI(
        base_url=secrets.gemini_api_url,
        api_key=secrets.gemini_api_key,
    )
    set_tracing_disabled(True)
    agent = Agent(
        name = "Assistant",
        instructions="Answer the question as best as you can.",
        model = OpenAIChatCompletionsModel(
            model=secrets.gemini_api_model,
            openai_client=external_client
        )
          
    )
    result = Runner.run_sync(
        starting_agent=agent,
        input=msg.content
    )
    
    message = cl.Message(
        content=result.final_output
    )
    
    await message.send()
