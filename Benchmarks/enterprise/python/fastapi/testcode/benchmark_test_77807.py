# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from lxml import etree


async def BenchmarkTest77807(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
