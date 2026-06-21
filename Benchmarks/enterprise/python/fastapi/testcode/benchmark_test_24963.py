# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach
from types import SimpleNamespace


async def BenchmarkTest24963(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
