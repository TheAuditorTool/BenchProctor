# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from starlette.responses import JSONResponse
import os


async def BenchmarkTest08887(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return JSONResponse({'config_set': 'APP_USER_PREFERENCE'}, status_code=200)
