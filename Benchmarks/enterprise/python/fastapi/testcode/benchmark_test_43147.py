# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from types import SimpleNamespace


async def BenchmarkTest43147(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        return HTMLResponse('<div>' + str(data) + '</div>')
    return await _evasion_task()
