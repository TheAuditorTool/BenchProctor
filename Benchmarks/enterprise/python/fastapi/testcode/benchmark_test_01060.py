# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest01060(request: Request):
    origin_value = request.headers.get('origin', '')
    data = ' '.join(str(origin_value).split())
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return JSONResponse({'lookup': arr[idx]}, status_code=200)
