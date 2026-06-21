# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest41421(request: Request):
    path_value = request.path_params.get('id', '')
    data = '%s' % str(path_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
