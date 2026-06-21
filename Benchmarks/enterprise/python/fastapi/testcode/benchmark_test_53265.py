# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest53265(request: Request, field: str = Form('')):
    field_value = field
    parts = str(field_value).split(',')
    data = ','.join(parts)
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
