import chainlit as cl
from rich import print
from my_secrets import Secrets
from agents import (
    Agent,
    OpenAIChatCompletionsModel,
    AsyncOpenAI,
    set_tracing_disabled,
    Runner,
)
from typing import cast


@cl.on_chat_start
async def start():
    secrets = Secrets()
    external_client = AsyncOpenAI(
        base_url=secrets.gemini_api_url,
        api_key=secrets.gemini_api_key,
    )
    set_tracing_disabled(True)
    agent = Agent(
        name="Assistant",
        instructions="Answer the question as best as you can.",
        model=OpenAIChatCompletionsModel(
            model=secrets.gemini_api_model, openai_client=external_client
        ),
    )

    cl.user_session.set("agent", agent)

    cl.user_session.set("chat_history", [])

    await cl.Message(
        content="Gemini API Chatbot",
    ).send()


@cl.on_message
async def main(msg: cl.Message):

    agent = cast(Agent, cl.user_session.get("agent"))

    chat_history: list = cl.user_session.get("chat_history") or []

    chat_history.append(
        {
            "role": "user",
            "content": msg.content,
        }
    )

    result = Runner.run_sync(starting_agent=agent, input=chat_history)
    
    cl.user_session.set("chat_history",result.to_input_list())
    
    print(chat_history)

    message = cl.Message(content=result.final_output)

    await message.send()
