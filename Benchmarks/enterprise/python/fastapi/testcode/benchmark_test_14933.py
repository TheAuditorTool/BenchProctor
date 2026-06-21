# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest14933(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value}'
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
