# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import time


def ensure_str(value):
    return str(value)

async def BenchmarkTest18735(request: Request):
    host_value = request.headers.get('host', '')
    data = ensure_str(host_value)
    if time.time() > 1000000000:
        return HTMLResponse('<div>' + str(data) + '</div>')
    return {"updated": True}
