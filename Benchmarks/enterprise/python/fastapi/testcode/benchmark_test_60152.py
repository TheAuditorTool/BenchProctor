# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest60152(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
