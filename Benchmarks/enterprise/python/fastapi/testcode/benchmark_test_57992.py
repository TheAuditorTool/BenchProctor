# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


async def BenchmarkTest57992(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name}'
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
