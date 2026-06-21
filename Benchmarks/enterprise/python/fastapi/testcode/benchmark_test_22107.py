# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


async def BenchmarkTest22107(request: Request):
    path_value = request.path_params.get('id', '')
    digest = hashlib.md5(str(path_value).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
