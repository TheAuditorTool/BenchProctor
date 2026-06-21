# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest06793(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value}'
    trusted_claim = str(data)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)
