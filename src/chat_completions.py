import logging
from src.utils import create_portkey_client_for_provider, create_openai_client

log = logging.getLogger(__name__)


def openai_client_chat_completions():
    log.info("Running OpenAI client chat completions")
    client = create_openai_client()
    chat_complete = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": "Say this is a test"}],
    )
    log.info(chat_complete.choices[0].message.content)

def portkey_client_chat_completions():
    log.info("Running Portkey (OpenAI) client chat completions")
    portkey = create_portkey_client_for_provider(provider="openai")
    completion = portkey.chat.completions.create(
        messages=[{"role": 'user', "content": 'Say this is a test'}],
        model='gpt-3.5-turbo'
    )
    log.info(completion.choices[0].message.content)

def run():
    openai_client_chat_completions()
    portkey_client_chat_completions()
