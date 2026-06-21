# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest03733(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = str(forwarded_ip).replace('\x00', '')
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return JSONResponse({'config_set': 'APP_USER_PREFERENCE'}, status_code=200)
