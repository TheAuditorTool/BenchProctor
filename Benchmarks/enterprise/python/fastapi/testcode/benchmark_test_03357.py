# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from urllib.parse import unquote
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest03357(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JSONResponse({'token': str(token)}, status_code=200)
