# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest76831(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = coalesce_blank(forwarded_ip)
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
