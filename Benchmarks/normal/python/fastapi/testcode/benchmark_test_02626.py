# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from fastapi import Form
from starlette.responses import JSONResponse
import re


async def BenchmarkTest02626(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JSONResponse({'validated': str(data)}, status_code=200)
    return {"updated": True}
