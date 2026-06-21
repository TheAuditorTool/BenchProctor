# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


async def BenchmarkTest48878(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value:.200s}'
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
