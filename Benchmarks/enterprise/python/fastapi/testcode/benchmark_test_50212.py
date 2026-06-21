# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


async def BenchmarkTest50212(request: Request, field: str = Form('')):
    field_value = field
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(field_value))
    return resp
