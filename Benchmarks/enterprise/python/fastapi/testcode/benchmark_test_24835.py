# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest24835(request: Request):
    path_value = request.path_params.get('id', '')
    data = RequestPayload(path_value).value
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
