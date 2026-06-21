# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest00814(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    if not auth_check(request.session.get('user', ''), str(multipart_value)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
