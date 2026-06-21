# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest45911(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = default_blank(header_value)
    processed = data[:64]
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return JSONResponse({'validated': str(processed)}, status_code=200)
    return {"updated": True}
