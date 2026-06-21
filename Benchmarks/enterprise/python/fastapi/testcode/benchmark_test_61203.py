# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest61203(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = ensure_str(auth_header)
    trusted_claim = str(data)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)
