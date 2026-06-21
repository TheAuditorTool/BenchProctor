# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest49580(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = to_text(raw_body)
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
