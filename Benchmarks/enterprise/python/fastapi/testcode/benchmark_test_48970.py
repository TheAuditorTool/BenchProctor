# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
import os
from starlette.responses import JSONResponse


async def BenchmarkTest48970(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', env_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = env_value
    eval(str(processed))
    return {"updated": True}
