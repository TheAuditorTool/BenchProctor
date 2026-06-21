# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest01657(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = RequestPayload(header_value).value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
