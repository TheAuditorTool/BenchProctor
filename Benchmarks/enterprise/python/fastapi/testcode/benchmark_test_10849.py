# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest10849(request: Request):
    referer_value = request.headers.get('referer', '')
    data = RequestPayload(referer_value).value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
