# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from urllib.parse import unquote
import os


async def BenchmarkTest59305(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
