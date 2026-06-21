# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


async def BenchmarkTest10729(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return HTMLResponse(str(processed))
