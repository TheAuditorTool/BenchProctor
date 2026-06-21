# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
import json
from starlette.responses import JSONResponse


async def BenchmarkTest05295(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return JSONResponse({'token': str(token)}, status_code=200)
