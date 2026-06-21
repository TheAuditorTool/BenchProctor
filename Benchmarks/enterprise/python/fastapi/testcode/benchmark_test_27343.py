# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest27343(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    raise RuntimeError('processing failed: ' + str(forwarded_ip))
    return {"updated": True}
