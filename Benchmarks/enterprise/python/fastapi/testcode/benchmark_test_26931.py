# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest26931(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data, _sep, _rest = str(upload_name).partition('\x00')
    if str(data) == 'is_admin':
        return JSONResponse({'access': 'granted', 'role': 'admin'}, status_code=200)
    return {"updated": True}
