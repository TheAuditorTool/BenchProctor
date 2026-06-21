# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest29947(request: Request):
    user_id = request.query_params.get('id', '')
    data = coalesce_blank(user_id)
    if auth_check('user', str(data)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
