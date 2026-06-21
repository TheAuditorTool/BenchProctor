# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import base64
import os


async def BenchmarkTest41903(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
