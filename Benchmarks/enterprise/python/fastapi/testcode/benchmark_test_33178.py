# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from dataclasses import dataclass
from fastapi import Form
from starlette.responses import JSONResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest33178(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JSONResponse({'token': str(token)}, status_code=200)
