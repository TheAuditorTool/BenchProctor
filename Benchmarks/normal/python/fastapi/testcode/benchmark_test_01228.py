# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest01228(request: Request):
    user_id = request.query_params.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    state = globals().setdefault('_lcg_state', [12345])
    state[0] = (state[0] * 1103515245 + (int(data) if str(data).isdigit() else 1)) % (2 ** 31)
    token = state[0]
    return JSONResponse({'token': str(token)}, status_code=200)
