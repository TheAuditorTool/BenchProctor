# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form
import os


async def BenchmarkTest36996(request: Request, field: str = Form('')):
    field_value = field
    data, _sep, _rest = str(field_value).partition('\x00')
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
