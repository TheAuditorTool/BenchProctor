# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
import json


async def BenchmarkTest12386(request: Request):
    host_value = request.headers.get('host', '')
    try:
        data = json.loads(host_value).get('value', host_value)
    except (json.JSONDecodeError, AttributeError):
        data = host_value
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
