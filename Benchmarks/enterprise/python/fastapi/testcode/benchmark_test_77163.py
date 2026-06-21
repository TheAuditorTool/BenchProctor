# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


async def BenchmarkTest77163(request: Request, field: str = Form('')):
    field_value = field
    data = ' '.join(str(field_value).split())
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
