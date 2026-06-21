# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest64046(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    entries = os.listdir(str(raw_body))
    return JSONResponse({'listing': entries}, status_code=200)
