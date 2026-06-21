# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import re
from starlette.responses import JSONResponse


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest02797(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = coalesce_blank(header_value)
    if not re.fullmatch('^[\\w\\s./\\\\:_?&=\\-@]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return RedirectResponse(url=str(processed))
