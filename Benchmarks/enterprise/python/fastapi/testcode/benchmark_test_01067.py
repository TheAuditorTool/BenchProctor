# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

async def BenchmarkTest01067(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
