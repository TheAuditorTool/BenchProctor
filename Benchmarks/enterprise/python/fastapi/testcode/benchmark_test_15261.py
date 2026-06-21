# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest15261(request: Request):
    host_value = request.headers.get('host', '')
    data = str(host_value).replace('\x00', '')
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
