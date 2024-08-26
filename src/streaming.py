import logging
from src.utils import create_portkey_client_for_provider, create_openai_client

log = logging.getLogger(__name__)


def openai_client_chat_completions_streaming():
    # https://platform.openai.com/docs/api-reference/streaming
    log.info("Running OpenAI client chat completions and streaming")
    client = create_openai_client()
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Say this is a test"}],
        stream=True,
    )
    log_streaming_response(stream)

def portkey_chat_completions_streaming():
    # https://docs.portkey.ai/docs/welcome/integration-guides/openai#streaming-responses
    log.info("Running Portkey (OpenAI) client chat completions with streaming")
    client = create_portkey_client_for_provider(provider="openai")
    stream = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Say this is a test"}],
        stream=True
    )
    log_streaming_response(stream)


def log_streaming_response(stream):
    accumulated_content = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            accumulated_content += chunk.choices[0].delta.content
            log.info("Received chunk: %s", chunk.choices[0].delta.content)
    log.info("Streaming finished! Full content:")
    log.info(accumulated_content)


def run():
    openai_client_chat_completions_streaming()
    portkey_chat_completions_streaming()
