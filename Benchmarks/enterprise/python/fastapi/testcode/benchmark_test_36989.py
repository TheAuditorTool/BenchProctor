# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re
from fastapi import Form


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest36989(request: Request, field: str = Form('')):
    field_value = field
    data = default_blank(field_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return JSONResponse({'error': 'schema invalid'}, status_code=400)
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
