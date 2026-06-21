# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest40599(request: Request):
    user_id = request.query_params.get('id', '')
    data = ensure_str(user_id)
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JSONResponse({'token': str(token)}, status_code=200)
