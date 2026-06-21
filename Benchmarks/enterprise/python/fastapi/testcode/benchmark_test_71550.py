# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest71550(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '{}'.format(referer_value)
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
