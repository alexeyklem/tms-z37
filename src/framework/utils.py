from typing import Any
from typing import Callable
from typing import Dict

from framework.consts import DIR_STATIC


def read_static(handler: str, converter: Callable = bytes) -> Any:
    path = DIR_STATIC / handler

    modes: Dict[Any, str] = {str: "r"}

    mode = modes.get(converter, "rb")

    with path.open(mode) as fp:
        payload = fp.read()

    return payload
