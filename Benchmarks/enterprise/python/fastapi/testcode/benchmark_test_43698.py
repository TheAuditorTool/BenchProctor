# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from dataclasses import dataclass
import os
from starlette.responses import JSONResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest43698(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JSONResponse({'token': str(token)}, status_code=200)
