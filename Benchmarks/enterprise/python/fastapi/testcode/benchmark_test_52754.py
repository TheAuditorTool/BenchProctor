# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


request_state: dict[str, str] = {}

async def BenchmarkTest52754(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    try:
        int(str(data))
    except ValueError:
        return JSONResponse({'error': 'invalid'}, status_code=400)
    return {"updated": True}
