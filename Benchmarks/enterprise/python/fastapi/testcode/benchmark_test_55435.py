# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest55435(request: Request):
    user_id = request.query_params.get('id', '')
    if not auth_check(request.session.get('user', ''), str(user_id)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
