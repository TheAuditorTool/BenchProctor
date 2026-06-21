# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest31290(request: Request, field: str = Form('')):
    field_value = field
    data = str(field_value).replace('\x00', '')
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
