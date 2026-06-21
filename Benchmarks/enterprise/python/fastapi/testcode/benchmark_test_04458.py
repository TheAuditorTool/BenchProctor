# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest04458(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = RequestPayload(config_value).value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
