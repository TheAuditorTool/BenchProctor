# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from lxml import etree


async def BenchmarkTest28362(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
