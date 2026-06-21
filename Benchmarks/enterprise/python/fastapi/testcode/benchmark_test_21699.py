# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest21699(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    if str(data) == 'S3cr3tToken':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
