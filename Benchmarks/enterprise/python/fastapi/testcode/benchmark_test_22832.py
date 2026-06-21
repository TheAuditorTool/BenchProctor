# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest22832(request: Request):
    referer_value = request.headers.get('referer', '')
    data = to_text(referer_value)
    state = globals().setdefault('_lcg_state', [12345])
    state[0] = (state[0] * 1103515245 + (int(data) if str(data).isdigit() else 1)) % (2 ** 31)
    token = state[0]
    return JSONResponse({'token': str(token)}, status_code=200)
