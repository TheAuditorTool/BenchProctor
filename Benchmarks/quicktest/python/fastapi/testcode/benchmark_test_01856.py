# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re


async def BenchmarkTest01856(request: Request):
    origin_value = request.headers.get('origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JSONResponse({'validated': str(data)}, status_code=200)
    return {"updated": True}
