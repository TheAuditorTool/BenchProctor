# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from lxml import etree


request_state: dict[str, str] = {}

async def BenchmarkTest45010(request: Request):
    host_value = request.headers.get('host', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
