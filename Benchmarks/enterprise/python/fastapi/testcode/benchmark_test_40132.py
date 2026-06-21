# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import re
from starlette.responses import JSONResponse


request_state: dict[str, str] = {}

async def BenchmarkTest40132(request: Request):
    origin_value = request.headers.get('origin', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s./\\\\:_?&=\\-@]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return RedirectResponse(url=str(processed))
