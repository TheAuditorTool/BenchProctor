# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest29095(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = raw_body.decode('utf-8', 'ignore') if isinstance(raw_body, bytes) else raw_body
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return JSONResponse({'lookup': arr[idx]}, status_code=200)
