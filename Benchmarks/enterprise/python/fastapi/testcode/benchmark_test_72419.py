# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


request_state: dict[str, str] = {}

async def BenchmarkTest72419(request: Request):
    path_value = request.path_params.get('id', '')
    request_state['last_input'] = path_value
    data = request_state['last_input']
    if request.session.get('user') is None:
        return JSONResponse({'error': 'no session'}, status_code=401)
    request.session['user'] = str(data)
    return {"updated": True}
