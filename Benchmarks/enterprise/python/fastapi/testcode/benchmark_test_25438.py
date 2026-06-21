# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import HTMLResponse


async def BenchmarkTest25438(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % (field_value,)
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
