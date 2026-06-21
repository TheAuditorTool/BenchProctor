# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import re
from starlette.responses import JSONResponse


async def BenchmarkTest48237(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(header_value)
    data = collected
    if not re.fullmatch('^[\\w\\s./\\\\:_?&=\\-@]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return RedirectResponse(url=str(processed))
