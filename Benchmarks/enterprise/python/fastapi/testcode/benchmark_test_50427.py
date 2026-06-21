# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest50427(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = ensure_str(auth_header)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JSONResponse({'token': str(token)}, status_code=200)
