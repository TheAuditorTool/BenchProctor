# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from fastapi import Form
from starlette.responses import JSONResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest14181(request: Request, field: str = Form('')):
    field_value = field
    data = ensure_str(field_value)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
