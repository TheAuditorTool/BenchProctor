# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest04946(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = f'{raw_body}'
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
