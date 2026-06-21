# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest74576(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = to_text(header_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return HTMLResponse(str(processed))
