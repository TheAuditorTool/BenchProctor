# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from fastapi import Form


async def BenchmarkTest10437(request: Request, field: str = Form('')):
    field_value = field
    data = '{}'.format(field_value)
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
