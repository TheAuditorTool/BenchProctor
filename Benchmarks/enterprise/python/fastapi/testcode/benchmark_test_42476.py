# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from lxml import etree


def to_text(value):
    return str(value).strip()

async def BenchmarkTest42476(request: Request):
    origin_value = request.headers.get('origin', '')
    data = to_text(origin_value)
    if os.environ.get("APP_ENV", "production") != "test":
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
