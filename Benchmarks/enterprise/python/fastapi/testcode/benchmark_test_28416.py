# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


def normalise_input(value):
    return value.strip()

async def BenchmarkTest28416(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = normalise_input(auth_header)
    processed = data[:64]
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return JSONResponse({'config_set': 'APP_USER_PREFERENCE'}, status_code=200)
