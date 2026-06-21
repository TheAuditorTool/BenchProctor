# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach
from types import SimpleNamespace


async def BenchmarkTest07845(request: Request):
    ua_value = request.headers.get('user-agent', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
