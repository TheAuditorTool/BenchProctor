# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest28201(request: Request):
    path_value = request.path_params.get('id', '')
    data = coalesce_blank(path_value)
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
