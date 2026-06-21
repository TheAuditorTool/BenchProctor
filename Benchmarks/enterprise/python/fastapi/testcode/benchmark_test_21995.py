# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest21995(request: Request):
    user_id = request.query_params.get('id', '')
    data = str(user_id).replace('\x00', '')
    if request.session.get('user') is None:
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
