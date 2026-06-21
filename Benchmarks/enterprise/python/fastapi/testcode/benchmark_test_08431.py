# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

async def BenchmarkTest08431(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = FormData(payload=forwarded_ip).payload
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
