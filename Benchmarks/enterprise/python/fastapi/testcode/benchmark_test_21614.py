# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest21614(request: Request):
    path_value = request.path_params.get('id', '')
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(path_value)})
