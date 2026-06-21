# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest23445(request: Request):
    path_value = request.path_params.get('id', '')
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return JSONResponse({'action': action}, status_code=200)
