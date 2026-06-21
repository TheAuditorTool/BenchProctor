# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest73310(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    pending = list(str(forwarded_ip).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return HTMLResponse('<div>' + str(data) + '</div>')
