# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from types import SimpleNamespace


async def BenchmarkTest03197(request: Request):
    user_id = request.query_params.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    _ev = {}
    eval(compile("_ev['r'] = HTMLResponse('<div>' + str(data) + '</div>')", '<sink>', 'exec'))
    return _ev['r']
