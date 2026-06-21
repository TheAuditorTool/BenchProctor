# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest39353(request: Request):
    path_value = request.path_params.get('id', '')
    data = default_blank(path_value)
    if str(data) in ('admin', 'true', 'authenticated'):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
