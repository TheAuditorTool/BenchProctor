# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest41175(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = ensure_str(multipart_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return JSONResponse({'error': 'schema invalid'}, status_code=400)
    if len(str(data)) >= 4:
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
