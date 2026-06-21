# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest51651(request: Request):
    user_id = request.query_params.get('id', '')
    data = RequestPayload(user_id).value
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
