# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest20502(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return JSONResponse({'action': action}, status_code=200)
