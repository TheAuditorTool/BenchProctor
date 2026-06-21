# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest45228(request: Request):
    host_value = request.headers.get('host', '')
    data = ' '.join(str(host_value).split())
    trusted_claim = str(data)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)
