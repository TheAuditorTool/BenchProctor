# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import time


def relay_value(value):
    return value

async def BenchmarkTest51556(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = relay_value(raw_body)
    if time.time() > 1000000000:
        return HTMLResponse('<div>' + str(data) + '</div>')
    return {"updated": True}
