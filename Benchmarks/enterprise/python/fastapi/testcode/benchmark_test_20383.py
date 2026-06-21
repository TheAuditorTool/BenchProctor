# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import pickle


request_state: dict[str, str] = {}

async def BenchmarkTest20383(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!()\\[\\]{}$-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    pickle.loads(processed.encode('latin-1'))
    return {"updated": True}
