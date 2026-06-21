# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


def relay_value(value):
    return value

async def BenchmarkTest06394(request: Request):
    user_id = request.query_params.get('id', '')
    data = relay_value(user_id)
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
