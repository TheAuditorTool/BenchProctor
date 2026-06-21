# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest24935(request: Request):
    referer_value = request.headers.get('referer', '')
    data = referer_value if referer_value else 'default'
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JSONResponse({'token': str(token)}, status_code=200)
