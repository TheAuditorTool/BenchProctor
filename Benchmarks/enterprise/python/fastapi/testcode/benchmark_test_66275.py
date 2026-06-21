# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest66275(request: Request, field: str = Form('')):
    field_value = field
    parts = str(field_value).split(',')
    data = ','.join(parts)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    trusted_claim = str(processed)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)
