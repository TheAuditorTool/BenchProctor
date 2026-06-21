# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


request_state: dict[str, str] = {}

async def BenchmarkTest71878(request: Request):
    origin_value = request.headers.get('origin', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    processed = data[:64]
    digest = hashlib.md5(str(processed).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
