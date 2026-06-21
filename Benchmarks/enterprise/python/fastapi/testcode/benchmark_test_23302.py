# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest23302(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JSONResponse({'action': action}, status_code=200)
