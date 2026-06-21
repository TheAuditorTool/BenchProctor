# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from urllib.parse import unquote


async def BenchmarkTest24358(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
