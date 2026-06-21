# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
from lxml import etree


def ensure_str(value):
    return str(value)

async def BenchmarkTest09759(request: Request):
    user_id = request.query_params.get('id', '')
    data = ensure_str(user_id)
    if time.time() > 1000000000:
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
