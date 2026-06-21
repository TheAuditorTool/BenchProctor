# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from fastapi import Form
from starlette.responses import JSONResponse


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest43139(request: Request, field: str = Form('')):
    field_value = field
    data = default_blank(field_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
