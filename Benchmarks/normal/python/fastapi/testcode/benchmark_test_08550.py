# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest08550(request: Request):
    path_value = request.path_params.get('id', '')
    trusted_claim = str(path_value)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)
