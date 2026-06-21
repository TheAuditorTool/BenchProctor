# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from fastapi import Form
from starlette.responses import JSONResponse


request_state: dict[str, str] = {}

async def BenchmarkTest67059(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JSONResponse({'token': str(token)}, status_code=200)
