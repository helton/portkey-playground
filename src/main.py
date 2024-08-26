from src.chat_completions import run as run_chat_completion_tests
from src.streaming import run as run_streaming_tests
from src.utils import setup_logging

if __name__ == "__main__":
    setup_logging()
    run_chat_completion_tests()
    run_streaming_tests()
