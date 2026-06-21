# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest34165(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return JSONResponse({'token': str(token)}, status_code=200)
