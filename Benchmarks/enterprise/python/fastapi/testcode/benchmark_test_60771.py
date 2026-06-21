# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest60771(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    if str(data) == 'S3cr3tToken':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
