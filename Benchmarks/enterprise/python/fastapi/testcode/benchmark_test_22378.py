# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


def relay_value(value):
    return value

async def BenchmarkTest22378(request: Request, field: str = Form('')):
    field_value = field
    data = relay_value(field_value)
    processed = data[:64]
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(processed), max_age=86400)
    return resp
