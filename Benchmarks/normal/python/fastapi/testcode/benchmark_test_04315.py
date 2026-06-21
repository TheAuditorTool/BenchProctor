# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest04315(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    os.environ['APP_USER_PREFERENCE'] = str(cookie_value)
    return JSONResponse({'config_set': 'APP_USER_PREFERENCE'}, status_code=200)
