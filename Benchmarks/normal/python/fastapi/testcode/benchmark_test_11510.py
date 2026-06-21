# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
import json
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


async def BenchmarkTest11510(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    return HTMLResponse(str(processed))
