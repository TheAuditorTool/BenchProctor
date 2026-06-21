# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest55715(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    random.seed(int(xml_value) if str(xml_value).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JSONResponse({'token': str(token)}, status_code=200)
