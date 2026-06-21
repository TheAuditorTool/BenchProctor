# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from dataclasses import dataclass
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest01395(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = FormData(payload=header_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    return HTMLResponse(str(processed))
