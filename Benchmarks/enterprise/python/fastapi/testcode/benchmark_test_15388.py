# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest15388(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = ' '.join(str(ua_value).split())
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
