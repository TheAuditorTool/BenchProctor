# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from dataclasses import dataclass
import os
from starlette.responses import JSONResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest68470(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
