# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


def ensure_str(value):
    return str(value)

async def BenchmarkTest48045(request: Request):
    origin_value = request.headers.get('origin', '')
    data = ensure_str(origin_value)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
