# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest42767(request: Request):
    path_value = request.path_params.get('id', '')
    data = '{}'.format(path_value)
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(data)})
