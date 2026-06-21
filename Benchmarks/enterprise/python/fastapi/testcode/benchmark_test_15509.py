# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from lxml import etree


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest15509(request: Request):
    path_value = request.path_params.get('id', '')
    data = default_blank(path_value)
    if os.environ.get("APP_ENV", "production") != "test":
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
