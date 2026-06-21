# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse
import re


async def BenchmarkTest49052(request: Request, field: str = Form('')):
    field_value = field
    data = str(field_value).replace('\x00', '')
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JSONResponse({'validated': str(data)}, status_code=200)
    return {"updated": True}
