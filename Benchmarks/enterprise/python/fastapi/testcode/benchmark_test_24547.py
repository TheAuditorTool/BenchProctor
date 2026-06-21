# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach
from types import SimpleNamespace


async def BenchmarkTest24547(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
