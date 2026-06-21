# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


def relay_value(value):
    return value

async def BenchmarkTest30058(request: Request, field: str = Form('')):
    field_value = field
    data = relay_value(field_value)
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
