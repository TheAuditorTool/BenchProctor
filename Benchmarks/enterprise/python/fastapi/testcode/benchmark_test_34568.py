# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest34568(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header:.200s}'
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return JSONResponse({'config_set': 'APP_USER_PREFERENCE'}, status_code=200)
