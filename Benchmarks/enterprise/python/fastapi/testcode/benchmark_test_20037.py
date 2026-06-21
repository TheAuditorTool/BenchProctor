# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import time


def ensure_str(value):
    return str(value)

async def BenchmarkTest20037(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = ensure_str(raw_body)
    if time.time() > 1000000000:
        return HTMLResponse('<img src="' + str(data) + '">')
    return {"updated": True}
