# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import pickle


request_state: dict[str, str] = {}

async def BenchmarkTest10192(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!()\\[\\]{}$-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    pickle.loads(processed.encode('latin-1'))
    return {"updated": True}
