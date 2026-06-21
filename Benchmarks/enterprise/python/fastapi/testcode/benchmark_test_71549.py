# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest71549(request: Request):
    path_value = request.path_params.get('id', '')
    parts = []
    for token in str(path_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    trusted_claim = str(data)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)
