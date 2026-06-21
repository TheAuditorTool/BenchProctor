# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse
import time


request_state: dict[str, str] = {}

async def BenchmarkTest16269(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        return HTMLResponse('<script src="' + str(data) + '"></script>')
    return {"updated": True}
