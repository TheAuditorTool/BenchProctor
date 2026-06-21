# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest11639(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
