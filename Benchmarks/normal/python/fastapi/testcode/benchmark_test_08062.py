# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest08062(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    if str(data) == 'S3cr3tToken':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
