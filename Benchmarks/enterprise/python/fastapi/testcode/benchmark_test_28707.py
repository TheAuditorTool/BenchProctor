# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import os


request_state: dict[str, str] = {}

async def BenchmarkTest28707(request: Request):
    referer_value = request.headers.get('referer', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        return HTMLResponse('<div>' + str(data) + '</div>')
    return {"updated": True}
