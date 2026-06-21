# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest31638(request: Request):
    referer_value = request.headers.get('referer', '')
    data = normalise_input(referer_value)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JSONResponse({'token': str(token)}, status_code=200)
