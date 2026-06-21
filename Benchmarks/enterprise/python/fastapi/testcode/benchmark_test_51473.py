# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest51473(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = RequestPayload(graphql_var).value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
