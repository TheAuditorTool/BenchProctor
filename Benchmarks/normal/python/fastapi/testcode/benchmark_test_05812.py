# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


def relay_value(value):
    return value

async def BenchmarkTest05812(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = relay_value(raw_body)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
