# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


def ensure_str(value):
    return str(value)

async def BenchmarkTest74031(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = ensure_str(forwarded_ip)
    eval(compile('_parser = etree.XMLParser(resolve_entities=True, no_network=False)\netree.fromstring(str(data).encode(), _parser)', '<sink>', 'exec'))
    return {"updated": True}
