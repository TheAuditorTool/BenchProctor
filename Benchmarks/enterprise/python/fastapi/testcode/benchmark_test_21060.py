# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest21060(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return JSONResponse({'token': str(token)}, status_code=200)
