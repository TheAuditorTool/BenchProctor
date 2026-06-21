# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


async def BenchmarkTest44983(request: Request):
    upload_name = (await request.form()).get('upload', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(upload_name)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = upload_name
    values = str(processed).split(',')
    if values:
        return JSONResponse({'first': values[0], 'dropped': len(values) - 1}, status_code=200)
    return {"updated": True}
