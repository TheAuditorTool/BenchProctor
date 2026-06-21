# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest00287(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = (lambda v: v.strip())(xml_value)
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
