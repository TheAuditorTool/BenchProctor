# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest08194(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = ' '.join(str(auth_header).split())
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JSONResponse({'token': str(token)}, status_code=200)
