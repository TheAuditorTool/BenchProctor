# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from urllib.parse import unquote


async def BenchmarkTest59760(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
