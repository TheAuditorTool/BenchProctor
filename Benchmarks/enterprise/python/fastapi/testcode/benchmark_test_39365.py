# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import re
from starlette.responses import JSONResponse


async def BenchmarkTest39365(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(cookie_value)
    data = collected
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!()\\[\\]{}$-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    yaml.load(processed, Loader=yaml.UnsafeLoader)
    return {"updated": True}
