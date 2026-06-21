# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest58929(request: Request):
    path_value = request.path_params.get('id', '')
    parts = str(path_value).split(',')
    data = ','.join(parts)
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return JSONResponse({'lookup': arr[idx]}, status_code=200)
