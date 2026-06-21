# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest50385(request: Request):
    path_value = request.path_params.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    if request.session.get('user') is None:
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    request.session['data'] = str(data)
    return {"updated": True}
