# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest29604(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = f'{config_value}'
    if request.session.get('user') is None:
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
