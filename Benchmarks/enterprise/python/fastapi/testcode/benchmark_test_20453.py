# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest20453(request: Request):
    user_id = request.query_params.get('id', '')
    random.seed(int(user_id) if str(user_id).isdigit() else 42)
    token = str(random.random())
    return JSONResponse({'token': str(token)}, status_code=200)
