# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


async def BenchmarkTest17033(request: Request):
    upload_name = (await request.form()).get('upload', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(upload_name)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = upload_name
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(processed)})
