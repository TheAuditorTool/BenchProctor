# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach


def to_text(value):
    return str(value).strip()

async def BenchmarkTest35156(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = to_text(ua_value)
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
