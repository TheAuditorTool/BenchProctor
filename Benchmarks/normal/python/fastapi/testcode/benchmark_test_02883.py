# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest02883(request: Request, field: str = Form('')):
    field_value = field
    if not auth_check(request.session.get('user', ''), str(field_value)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
