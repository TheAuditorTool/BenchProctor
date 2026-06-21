# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import HTMLResponse


async def BenchmarkTest81111(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value}'
    return HTMLResponse(str(data))
