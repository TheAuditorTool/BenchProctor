# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest34477(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    os.environ['APP_USER_PREFERENCE'] = str(header_value)
    return JSONResponse({'config_set': 'APP_USER_PREFERENCE'}, status_code=200)
