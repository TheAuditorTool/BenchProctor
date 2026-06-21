# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach
from types import SimpleNamespace


async def BenchmarkTest01462(request: Request):
    referer_value = request.headers.get('referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
