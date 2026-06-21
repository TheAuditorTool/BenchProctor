# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest22484(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value}'
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JSONResponse({'token': str(token)}, status_code=200)
