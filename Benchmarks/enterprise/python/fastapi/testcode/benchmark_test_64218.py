# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import importlib


request_state: dict[str, str] = {}

async def BenchmarkTest64218(request: Request):
    referer_value = request.headers.get('referer', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-{}()=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    importlib.import_module(str(processed))
    return {"updated": True}
