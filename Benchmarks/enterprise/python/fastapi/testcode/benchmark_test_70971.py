# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import os


request_state: dict[str, str] = {}

async def BenchmarkTest70971(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        return HTMLResponse('<img src="' + str(data) + '">')
    return {"updated": True}
