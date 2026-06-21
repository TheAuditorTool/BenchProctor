# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest08187(request: Request):
    path_value = request.path_params.get('id', '')
    return JSONResponse({'error': str(path_value), 'stack': repr(locals())}, status_code=500)
