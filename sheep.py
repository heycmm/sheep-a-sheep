from mitmproxy import ctx
from config import first_map_url, second_map_url


def request(flow):
    if flow.request.url.startswith(second_map_url):
        flow.request.url = first_map_url
        ctx.log.info("修改链接")


class Sheep:
    pass


addons = [
    Sheep()
]

