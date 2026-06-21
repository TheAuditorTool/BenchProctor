# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest53095(request: Request):
    referer_value = request.headers.get('referer', '')
    data = coalesce_blank(referer_value)
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JSONResponse({'validated': str(data)}, status_code=200)
    return {"updated": True}
