# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import time


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest76571(request: Request):
    referer_value = request.headers.get('referer', '')
    data = default_blank(referer_value)
    if time.time() > 1000000000:
        return HTMLResponse('<div>' + str(data) + '</div>')
    return {"updated": True}
