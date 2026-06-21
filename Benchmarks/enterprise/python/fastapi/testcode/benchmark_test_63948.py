# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from lxml import etree


def normalise_input(value):
    return value.strip()

async def BenchmarkTest63948(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = normalise_input(auth_header)
    if os.environ.get("APP_ENV", "production") != "test":
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
