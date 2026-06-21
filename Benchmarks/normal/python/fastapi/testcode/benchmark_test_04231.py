# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import re
import os
from starlette.responses import JSONResponse


async def BenchmarkTest04231(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', env_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = env_value
    return HTMLResponse('<div>' + str(processed) + '</div>')
