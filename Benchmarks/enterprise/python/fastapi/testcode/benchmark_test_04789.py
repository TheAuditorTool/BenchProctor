# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest04789(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value}'
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(data)})
