# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest15481(request: Request):
    auth_header = request.headers.get('authorization', '')
    random.seed(int(auth_header) if str(auth_header).isdigit() else 42)
    token = str(random.random())
    return JSONResponse({'token': str(token)}, status_code=200)
