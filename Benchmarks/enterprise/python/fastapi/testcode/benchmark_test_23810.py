# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest23810(request: Request):
    user_id = request.query_params.get('id', '')
    data = RequestPayload(user_id).value
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
