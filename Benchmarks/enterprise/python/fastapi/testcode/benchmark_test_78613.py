# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import base64
import os


async def BenchmarkTest78613(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
