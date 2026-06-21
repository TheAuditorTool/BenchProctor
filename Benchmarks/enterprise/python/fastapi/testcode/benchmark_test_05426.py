# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


async def BenchmarkTest05426(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value:.200s}'
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    arr = [10, 20, 30, 40, 50]
    idx = int(str(processed))
    return JSONResponse({'lookup': arr[idx]}, status_code=200)
