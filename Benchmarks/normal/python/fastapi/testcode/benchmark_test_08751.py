# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest08751(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = ensure_str(raw_body)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JSONResponse({'token': str(token)}, status_code=200)
