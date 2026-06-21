# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
import os
from starlette.responses import JSONResponse


async def BenchmarkTest61827(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
