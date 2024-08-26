import logging
import os
from typing import Optional

from openai import OpenAI
from portkey_ai import createHeaders, Portkey

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PORTKEY_GATEWAY_URL = os.getenv("PORTKEY_GATEWAY_URL")

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')


def create_portkey_client_for_provider(provider: str) -> Optional[Portkey]:
    client: Portkey
    match provider:
        case "openai":
            client = Portkey(
                base_url=PORTKEY_GATEWAY_URL,
                api_key="no key",
                provider="openai",
                Authorization=OPENAI_API_KEY
            )
        case _:
            raise ValueError(f"Unknown provider: {provider}")
    return client

def create_openai_client() -> OpenAI:
        return OpenAI(
            api_key=OPENAI_API_KEY,
            base_url=PORTKEY_GATEWAY_URL,
            default_headers=createHeaders(
                provider="openai"
            )
        )
