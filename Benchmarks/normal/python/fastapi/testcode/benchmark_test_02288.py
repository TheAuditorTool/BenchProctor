# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest02288(request: Request):
    origin_value = request.headers.get('origin', '')
    data = to_text(origin_value)
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(data)})
