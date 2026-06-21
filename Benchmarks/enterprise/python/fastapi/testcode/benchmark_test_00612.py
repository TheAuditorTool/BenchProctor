# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import re
import os
from starlette.responses import JSONResponse


async def BenchmarkTest00612(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    kind = 'json' if str(env_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = env_value
            data = parsed
        case _:
            data = env_value
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return HTMLResponse(Template(processed).render())
