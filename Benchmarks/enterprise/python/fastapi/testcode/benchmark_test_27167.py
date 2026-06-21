# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest27167(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = RequestPayload(cookie_value).value
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
