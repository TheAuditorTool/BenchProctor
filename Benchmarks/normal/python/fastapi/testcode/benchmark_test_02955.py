# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


async def BenchmarkTest02955(request: Request):
    path_value = request.path_params.get('id', '')
    data = path_value if path_value else 'default'
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
