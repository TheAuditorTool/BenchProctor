# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form
from starlette.responses import HTMLResponse


async def BenchmarkTest28850(request: Request, field: str = Form('')):
    field_value = field
    data, _sep, _rest = str(field_value).partition('\x00')
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
