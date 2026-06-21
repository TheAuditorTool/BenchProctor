# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


def normalise_input(value):
    return value.strip()

async def BenchmarkTest18714(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = normalise_input(ua_value)
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
