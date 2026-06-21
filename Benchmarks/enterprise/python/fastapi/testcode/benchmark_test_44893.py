# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest44893(request: Request):
    referer_value = request.headers.get('referer', '')
    random.seed(int(referer_value) if str(referer_value).isdigit() else 7)
    token = random.getrandbits(8)
    return JSONResponse({'token': str(token)}, status_code=200)
