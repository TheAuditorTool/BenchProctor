# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest44940(request: Request):
    path_value = request.path_params.get('id', '')
    if path_value not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = path_value
    eval(str(processed))
    return {"updated": True}
