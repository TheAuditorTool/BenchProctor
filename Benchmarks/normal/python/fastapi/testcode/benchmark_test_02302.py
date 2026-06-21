# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse
import re


async def BenchmarkTest02302(request: Request, field: str = Form('')):
    field_value = field
    if re.search('[a-zA-Z0-9_-]+', str(field_value)):
        return JSONResponse({'validated': str(field_value)}, status_code=200)
    return {"updated": True}
