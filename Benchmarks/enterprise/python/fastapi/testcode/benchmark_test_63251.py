# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest63251(request: Request, field: str = Form('')):
    field_value = field
    data = default_blank(field_value)
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
