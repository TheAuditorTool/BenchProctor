# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest33112(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % (host_value,)
    trusted_claim = str(data)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)
