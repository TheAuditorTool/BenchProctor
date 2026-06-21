# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest06954(request: Request, field: str = Form('')):
    field_value = field
    data, _sep, _rest = str(field_value).partition('\x00')
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
