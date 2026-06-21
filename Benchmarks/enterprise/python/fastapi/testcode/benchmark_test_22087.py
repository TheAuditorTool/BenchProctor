# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest22087(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
