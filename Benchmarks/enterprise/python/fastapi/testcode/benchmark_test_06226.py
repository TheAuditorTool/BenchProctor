# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest06226(request: Request):
    origin_value = request.headers.get('origin', '')
    if origin_value not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = origin_value
    os.unlink('/var/app/data/' + str(processed))
    return {"updated": True}
