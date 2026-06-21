# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from fastapi import Form


async def BenchmarkTest58342(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    return HTMLResponse('<div>' + str(data) + '</div>')
