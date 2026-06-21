# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
import os
from starlette.responses import JSONResponse


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest76291(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(processed)})
