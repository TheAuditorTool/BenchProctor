# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest14243(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = RequestPayload(graphql_var).value
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
