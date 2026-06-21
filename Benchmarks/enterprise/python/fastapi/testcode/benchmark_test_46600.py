# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest46600(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = RequestPayload(multipart_value).value
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
