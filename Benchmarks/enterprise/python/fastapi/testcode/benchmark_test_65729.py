# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from starlette.responses import JSONResponse


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest65729(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = default_blank(cookie_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    os.system('echo ' + str(processed))
    return {"updated": True}
