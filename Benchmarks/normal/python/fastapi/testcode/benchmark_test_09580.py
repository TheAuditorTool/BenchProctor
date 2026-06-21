# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest09580(request: Request):
    user_id = request.query_params.get('id', '')
    data = RequestPayload(user_id).value
    json.loads(data)
    return {"updated": True}
