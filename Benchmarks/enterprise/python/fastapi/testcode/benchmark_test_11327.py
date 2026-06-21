# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest11327(request: Request):
    user_id = request.query_params.get('id', '')
    data = RequestPayload(user_id).value
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
