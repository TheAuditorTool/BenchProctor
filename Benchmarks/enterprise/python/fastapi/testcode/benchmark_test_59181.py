# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest59181(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = RequestPayload(dotenv_value).value
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
