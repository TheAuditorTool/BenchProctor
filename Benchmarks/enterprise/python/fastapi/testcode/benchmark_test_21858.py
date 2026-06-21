# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


def normalise_input(value):
    return value.strip()

async def BenchmarkTest21858(request: Request, field: str = Form('')):
    field_value = field
    data = normalise_input(field_value)
    request.session.clear()
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
