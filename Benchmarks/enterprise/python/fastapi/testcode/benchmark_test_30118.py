# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form
from starlette.responses import HTMLResponse


async def BenchmarkTest30118(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
