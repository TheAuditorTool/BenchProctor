# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest49362(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
