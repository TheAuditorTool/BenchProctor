# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


async def BenchmarkTest78489(request: Request, field: str = Form('')):
    field_value = field
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
