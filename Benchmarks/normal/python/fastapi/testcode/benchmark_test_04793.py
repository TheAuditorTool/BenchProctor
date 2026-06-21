# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest04793(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = default_blank(multipart_value)
    if not auth_check(request.session.get('user', ''), str(data)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
