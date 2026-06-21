# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
from starlette.responses import JSONResponse


async def BenchmarkTest67078(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    values = str(data).split(',')
    if values:
        return JSONResponse({'first': values[0], 'dropped': len(values) - 1}, status_code=200)
    return {"updated": True}
