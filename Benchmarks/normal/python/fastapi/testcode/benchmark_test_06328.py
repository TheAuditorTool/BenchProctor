# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest06328(request: Request):
    stdin_value = input('input: ')
    data = RequestPayload(stdin_value).value
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return {"updated": True}
