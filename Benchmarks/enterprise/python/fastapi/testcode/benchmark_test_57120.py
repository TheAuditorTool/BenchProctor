# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest57120(request: Request):
    referer_value = request.headers.get('referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return JSONResponse({'config_set': 'APP_USER_PREFERENCE'}, status_code=200)
