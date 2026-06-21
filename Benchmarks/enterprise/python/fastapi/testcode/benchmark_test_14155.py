# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from urllib.parse import unquote
import os


async def BenchmarkTest14155(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
