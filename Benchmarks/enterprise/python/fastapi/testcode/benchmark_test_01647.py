# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest01647(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = header_value if header_value else 'default'
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JSONResponse({'token': str(token)}, status_code=200)
