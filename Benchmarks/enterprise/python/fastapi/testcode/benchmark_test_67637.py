# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest67637(request: Request):
    host_value = request.headers.get('host', '')
    data = default_blank(host_value)
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
