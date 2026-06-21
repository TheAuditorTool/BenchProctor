# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from fastapi import Form


async def BenchmarkTest03740(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value:.200s}'
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
