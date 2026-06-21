# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest64212(request: Request):
    path_value = request.path_params.get('id', '')
    data = ' '.join(str(path_value).split())
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
