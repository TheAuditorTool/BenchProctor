# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest42582(request: Request):
    user_id = request.query_params.get('id', '')
    data = RequestPayload(user_id).value
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
