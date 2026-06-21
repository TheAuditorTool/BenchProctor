# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest48032(request: Request, field: str = Form('')):
    field_value = field
    digest = hashlib.sha256(('static_salt_123' + str(field_value)).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
