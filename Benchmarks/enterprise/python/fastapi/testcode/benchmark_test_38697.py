# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form
from starlette.responses import HTMLResponse


async def BenchmarkTest38697(request: Request, field: str = Form('')):
    field_value = field
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
