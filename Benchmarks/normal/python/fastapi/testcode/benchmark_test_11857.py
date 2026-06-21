# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest11857(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = str(auth_header).replace('\x00', '')
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JSONResponse({'token': str(token)}, status_code=200)
