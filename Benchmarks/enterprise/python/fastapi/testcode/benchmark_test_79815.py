# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from lxml import etree


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest79815(request: Request, field: str = Form('')):
    field_value = field
    data = RequestPayload(field_value).value
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
