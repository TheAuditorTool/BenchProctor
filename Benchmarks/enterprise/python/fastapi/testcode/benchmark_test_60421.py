# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest60421(request: Request):
    ua_value = request.headers.get('user-agent', '')
    random.seed(int(ua_value) if str(ua_value).isdigit() else 42)
    token = str(random.random())
    return JSONResponse({'token': str(token)}, status_code=200)
