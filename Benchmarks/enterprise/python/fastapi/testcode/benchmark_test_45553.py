# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


async def BenchmarkTest45553(request: Request):
    user_id = request.query_params.get('id', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(user_id).encode(), _parser)
    return {"updated": True}
