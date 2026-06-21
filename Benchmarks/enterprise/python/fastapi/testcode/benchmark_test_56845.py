# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest56845(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = f'{raw_body}'
    if request.session.get('user') is None:
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    request.session.clear()
    request.session['user'] = str(data)
    return {"updated": True}
