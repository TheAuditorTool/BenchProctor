# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest73981(request: Request):
    host_value = request.headers.get('host', '')
    data = coalesce_blank(host_value)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
