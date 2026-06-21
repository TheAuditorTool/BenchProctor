# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest00801(request: Request):
    auth_header = request.headers.get('authorization', '')
    random.seed(int(auth_header) if str(auth_header).isdigit() else 99)
    token = random.randint(0, 99)
    return JSONResponse({'token': str(token)}, status_code=200)
