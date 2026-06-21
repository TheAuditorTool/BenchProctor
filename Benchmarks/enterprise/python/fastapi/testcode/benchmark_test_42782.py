# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest42782(request: Request):
    user_id = request.query_params.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
