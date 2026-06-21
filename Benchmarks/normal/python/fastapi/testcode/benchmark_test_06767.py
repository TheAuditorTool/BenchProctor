# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest06767(request: Request, field: str = Form('')):
    field_value = field
    random.seed(int(field_value) if str(field_value).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JSONResponse({'token': str(token)}, status_code=200)
