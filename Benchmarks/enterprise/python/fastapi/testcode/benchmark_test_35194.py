# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest35194(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = env_value
    os.system('echo ' + str(processed))
    return {"updated": True}
