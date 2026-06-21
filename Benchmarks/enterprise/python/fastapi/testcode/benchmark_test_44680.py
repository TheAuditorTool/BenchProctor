# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest44680(request: Request):
    auth_header = request.headers.get('authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return JSONResponse({'token': str(token)}, status_code=200)
