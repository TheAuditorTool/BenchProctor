# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


async def BenchmarkTest08477(request: Request):
    path_value = request.path_params.get('id', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', path_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = path_value
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
