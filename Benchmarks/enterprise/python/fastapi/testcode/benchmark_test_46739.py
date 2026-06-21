# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest46739(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
