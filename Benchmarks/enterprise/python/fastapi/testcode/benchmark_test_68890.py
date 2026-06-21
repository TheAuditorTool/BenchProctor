# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest68890(request: Request):
    host_value = request.headers.get('host', '')
    data = relay_value(host_value)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JSONResponse({'token': str(token)}, status_code=200)
