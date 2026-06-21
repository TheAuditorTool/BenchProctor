# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest16495(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id:.200s}'
    if request.session.get('role') != 'admin':
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    request.session['data'] = str(data)
    return {"updated": True}
