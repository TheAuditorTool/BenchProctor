# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest66949(request: Request):
    host_value = request.headers.get('host', '')
    reader = make_reader(host_value)
    data = reader()
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
