# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest31822(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    random.seed(int(raw_body) if str(raw_body).isdigit() else 99)
    token = random.randint(0, 99)
    return JSONResponse({'token': str(token)}, status_code=200)
