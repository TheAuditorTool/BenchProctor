# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest81114(request: Request):
    referer_value = request.headers.get('referer', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(referer_value)
    data = collected
    if request.session.get('user') is None:
        return JSONResponse({'error': 'no session'}, status_code=401)
    request.session['user'] = str(data)
    return {"updated": True}
