# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest10295(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    random.seed(int(xml_value) if str(xml_value).isdigit() else 7)
    token = random.getrandbits(8)
    return JSONResponse({'token': str(token)}, status_code=200)
