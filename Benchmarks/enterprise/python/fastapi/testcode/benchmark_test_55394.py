# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


def to_text(value):
    return str(value).strip()

async def BenchmarkTest55394(request: Request):
    origin_value = request.headers.get('origin', '')
    data = to_text(origin_value)
    processed = str(data).replace("<script", "")
    return HTMLResponse('<div>' + str(processed) + '</div>')
