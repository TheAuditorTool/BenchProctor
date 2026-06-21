# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest52443(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    random.seed(int(raw_body) if str(raw_body).isdigit() else 42)
    token = str(random.random())
    return JSONResponse({'token': str(token)}, status_code=200)
