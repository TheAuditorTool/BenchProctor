# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from urllib.parse import unquote
from fastapi import Form


async def BenchmarkTest01179(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
