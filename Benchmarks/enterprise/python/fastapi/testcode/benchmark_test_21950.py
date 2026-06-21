# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest21950(request: Request):
    user_id = request.query_params.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = True
    if not granted:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
