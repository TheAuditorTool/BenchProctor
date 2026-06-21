# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest23565(request: Request):
    auth_header = request.headers.get('authorization', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(auth_header)
    data = collected
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
