# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest02642(request: Request):
    upload_name = (await request.form()).get('upload', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(upload_name)
    data = collected
    if str(data) == 'S3cr3tToken':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
