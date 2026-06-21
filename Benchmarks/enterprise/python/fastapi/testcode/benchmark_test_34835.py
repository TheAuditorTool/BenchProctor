# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest34835(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    if auth_check('user', str(xml_value)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
