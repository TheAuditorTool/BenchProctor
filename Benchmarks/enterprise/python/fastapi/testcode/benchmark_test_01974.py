# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import os
from types import SimpleNamespace


async def BenchmarkTest01974(request: Request):
    host_value = request.headers.get('host', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        return HTMLResponse('<div>' + str(data) + '</div>')
    return {"updated": True}
