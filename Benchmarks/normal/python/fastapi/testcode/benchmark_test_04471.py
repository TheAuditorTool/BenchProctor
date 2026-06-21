# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from fastapi import Form


async def BenchmarkTest04471(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    return HTMLResponse('<img src="' + str(data) + '">')
