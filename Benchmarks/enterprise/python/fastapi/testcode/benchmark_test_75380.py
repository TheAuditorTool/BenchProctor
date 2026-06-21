# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re


def to_text(value):
    return str(value).strip()

async def BenchmarkTest75380(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = to_text(header_value)
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JSONResponse({'validated': str(data)}, status_code=200)
    return {"updated": True}
