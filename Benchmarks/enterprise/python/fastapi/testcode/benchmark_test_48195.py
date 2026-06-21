# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import re
from starlette.responses import JSONResponse


request_state: dict[str, str] = {}

async def BenchmarkTest48195(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    return HTMLResponse('<div>' + str(processed) + '</div>')
