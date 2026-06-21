# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest42503(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    if str(data) == 'S3cr3tToken':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
