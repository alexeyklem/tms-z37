import random
from mimetypes import guess_type

from framework.consts import DIR_STATIC


def application(environ, start_response):

    handlers = {
        # "/xxx/": "Styles.css",
        # "/logo.png/": "logo.png",
        "/": handle_404,
    }
    url = environ["PATH_INFO"]

    handler = handlers.get(url, generate_404)

    status = "200 OK"
    headers = {
        "Content-type": "text/html",
    }

    payload = handler(environ)
    start_response(status, list(headers.items()))
    yield payload


def read_static(handler: str) -> bytes:
    path = DIR_STATIC / handler

    with path.open("rb") as fp:
        payload = fp.read()

    return payload


def handle_404(environ) -> bytes:
    base_html = read_static("_base.html").decode()
    index_html = read_static("index.html").decode()

    result = base_html.format(xxx=index_html)
    return result.encode()


def generate_404(environ) -> bytes:
    url = environ["PATH_INFO"]
    pincode = random.randint(1, 2000)

    msg = (
        f"Hello User! if your path: {url} , but your path not found. Pincode: {pincode}"
    )

    return msg.encode()
