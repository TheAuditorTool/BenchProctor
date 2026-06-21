# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


async def BenchmarkTest62714(request: Request, field: str = Form('')):
    field_value = field
    data = '{}'.format(field_value)
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return JSONResponse({'status': 'ok'}, status_code=200, headers={'Access-Control-Allow-Origin': origin})
    return {"updated": True}
