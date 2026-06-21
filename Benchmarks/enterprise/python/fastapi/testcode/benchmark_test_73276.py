# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import re
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest73276(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = relay_value(upload_name)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    return HTMLResponse('<div>' + str(processed) + '</div>')
