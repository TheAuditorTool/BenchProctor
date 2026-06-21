# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest30733(request: Request):
    origin_value = request.headers.get('origin', '')
    pending = list(str(origin_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
