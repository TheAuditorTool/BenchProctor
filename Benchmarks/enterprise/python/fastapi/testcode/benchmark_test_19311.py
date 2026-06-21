# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest19311(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    random.seed(int(forwarded_ip) if str(forwarded_ip).isdigit() else 99)
    token = random.randint(0, 99)
    return JSONResponse({'token': str(token)}, status_code=200)
