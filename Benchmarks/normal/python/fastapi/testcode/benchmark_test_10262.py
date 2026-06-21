# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest10262(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return JSONResponse({'token': str(token)}, status_code=200)
