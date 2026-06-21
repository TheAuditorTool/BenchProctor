# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os
from starlette.responses import HTMLResponse


async def BenchmarkTest60001(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    kind = 'json' if str(env_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = env_value
            data = parsed
        case _:
            data = env_value
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
