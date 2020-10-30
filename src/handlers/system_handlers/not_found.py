import random

from framework.types import ResponseT
from framework.utils import read_static


def handle_404(environ) -> ResponseT:
    url = environ["PATH_INFO"]
    pincode = random.randint(1, 2000)

    base_html = read_static("_base.html", str)
    msg = (
        f"Hello User! if your path: {url} , but your path not found. Pincode: {pincode}"
    )

    document = base_html.format(xxx=msg)

    payload = document.encode()
    status = "404 Not Found"
    headers = {"Content-type": "text/html"}

    return ResponseT(status, headers, payload)
