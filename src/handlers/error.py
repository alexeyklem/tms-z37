from framework.types import RequestT
from framework.types import ResponseT


def handle_error(_request: RequestT) -> ResponseT:
    1 / 0
