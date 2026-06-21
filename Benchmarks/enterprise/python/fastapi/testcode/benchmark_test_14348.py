# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest14348(request: Request):
    referer_value = request.headers.get('referer', '')
    raise RuntimeError('processing failed: ' + str(referer_value))
    return {"updated": True}
