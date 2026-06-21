# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest46728(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = normalise_input(multipart_value)
    if str(data) == 'S3cr3tToken':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
