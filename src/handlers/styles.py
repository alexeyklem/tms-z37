from framework.types import ResponseT
from framework.utils import read_static


def handle_styles(_environ) -> ResponseT:
    payload = read_static("Styless.css")
    status = "200 OK"
    headers = {"Content-type": "text/css"}

    return ResponseT(status, headers, payload)
