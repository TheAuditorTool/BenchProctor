# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest07485(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    if not auth_check('user', hashlib.sha256(str(xml_value).encode()).hexdigest()):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
