# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


async def BenchmarkTest46118(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data, _sep, _rest = str(upload_name).partition('\x00')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
