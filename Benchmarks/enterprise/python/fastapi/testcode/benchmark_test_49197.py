# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest49197(request: Request, field: str = Form('')):
    field_value = field
    if len(str(field_value)) >= 4:
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
