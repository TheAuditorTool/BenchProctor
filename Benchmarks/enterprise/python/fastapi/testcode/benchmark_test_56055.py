# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import os
from types import SimpleNamespace


async def BenchmarkTest56055(request: Request):
    auth_header = request.headers.get('authorization', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        return HTMLResponse('<div>' + str(data) + '</div>')
    return {"updated": True}
