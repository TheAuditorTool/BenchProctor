# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest12549(request: Request):
    path_value = request.path_params.get('id', '')
    prefix = ''
    data = prefix + str(path_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
