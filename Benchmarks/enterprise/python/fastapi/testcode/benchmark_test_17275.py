# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re


async def BenchmarkTest17275(request: Request):
    auth_header = request.headers.get('authorization', '')
    if re.search('[a-zA-Z0-9_-]+', str(auth_header)):
        return JSONResponse({'validated': str(auth_header)}, status_code=200)
    return {"updated": True}
