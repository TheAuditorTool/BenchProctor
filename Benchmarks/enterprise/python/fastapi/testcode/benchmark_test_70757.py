# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest70757(request: Request):
    host_value = request.headers.get('host', '')
    data = (lambda v: v.strip())(host_value)
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
