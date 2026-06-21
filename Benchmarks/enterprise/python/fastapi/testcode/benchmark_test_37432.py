# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


def relay_value(value):
    return value

async def BenchmarkTest37432(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = relay_value(multipart_value)
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = False
    if not granted:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
