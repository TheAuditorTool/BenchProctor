# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest18070(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
