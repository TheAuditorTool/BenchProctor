# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest10532(request: Request):
    referer_value = request.headers.get('referer', '')
    data = handle(referer_value)
    processed = data[:64]
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return {"updated": True}
