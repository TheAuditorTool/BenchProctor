# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from types import SimpleNamespace


async def BenchmarkTest03455(request: Request):
    user_id = request.query_params.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        return HTMLResponse('<div>' + str(data) + '</div>')
    return await _evasion_task()
