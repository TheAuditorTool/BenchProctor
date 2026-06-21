# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import re
from starlette.responses import JSONResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest45599(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    reader = make_reader(header_value)
    data = reader()
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return HTMLResponse('<img src="' + str(processed) + '">')
