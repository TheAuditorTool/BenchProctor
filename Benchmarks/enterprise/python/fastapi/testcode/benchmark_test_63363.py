# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest63363(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = RequestPayload(forwarded_ip).value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
