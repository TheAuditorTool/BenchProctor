# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest10662(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = normalise_input(auth_header)
    if str(data) == 'S3cr3tToken':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
