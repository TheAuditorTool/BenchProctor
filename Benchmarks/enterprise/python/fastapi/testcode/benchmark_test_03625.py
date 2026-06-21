# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import re
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


request_state: dict[str, str] = {}

async def BenchmarkTest03625(request: Request):
    upload_name = (await request.form()).get('upload', '')
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return HTMLResponse('<script src="' + str(processed) + '"></script>')
