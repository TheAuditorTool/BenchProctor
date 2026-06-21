# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest28022(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    try:
        result = int(str(raw_body))
    except ValueError as e:
        return JSONResponse({'error': str(e)}, status_code=400)
    return {"updated": True}
