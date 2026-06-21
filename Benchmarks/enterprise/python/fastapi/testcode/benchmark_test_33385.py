# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest33385(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = coalesce_blank(header_value)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JSONResponse({'token': str(token)}, status_code=200)
