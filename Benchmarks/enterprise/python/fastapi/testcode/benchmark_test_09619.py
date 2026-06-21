# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest09619(request: Request):
    referer_value = request.headers.get('referer', '')
    random.seed(int(referer_value) if str(referer_value).isdigit() else 99)
    token = random.randint(0, 99)
    return JSONResponse({'token': str(token)}, status_code=200)
