# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest31151(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    state = globals().setdefault('_lcg_state', [12345])
    state[0] = (state[0] * 1103515245 + (int(data) if str(data).isdigit() else 1)) % (2 ** 31)
    token = state[0]
    return JSONResponse({'token': str(token)}, status_code=200)
