# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form
from starlette.responses import HTMLResponse


async def BenchmarkTest49601(request: Request, field: str = Form('')):
    field_value = field
    data = str(field_value).replace('\x00', '')
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
