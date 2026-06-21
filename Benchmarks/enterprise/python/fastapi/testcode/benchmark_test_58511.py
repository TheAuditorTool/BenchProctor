# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


async def BenchmarkTest58511(request: Request):
    auth_header = request.headers.get('authorization', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(auth_header)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = auth_header
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
