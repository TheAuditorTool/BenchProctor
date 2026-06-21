# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach
from types import SimpleNamespace


async def BenchmarkTest78365(request: Request):
    path_value = request.path_params.get('id', '')
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
