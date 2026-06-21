# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest42359(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    try:
        granted = auth_check('resource', str(multipart_value))
    except Exception:
        granted = False
    if not granted:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
