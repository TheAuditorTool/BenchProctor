# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from dataclasses import dataclass
from starlette.responses import JSONResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest55196(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JSONResponse({'token': str(token)}, status_code=200)
