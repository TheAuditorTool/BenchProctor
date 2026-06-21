# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace


async def BenchmarkTest28626(request: Request):
    path_value = request.path_params.get('id', '')
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    request.session['user'] = str(data)
    return {"updated": True}
