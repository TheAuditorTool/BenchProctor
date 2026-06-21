# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


async def BenchmarkTest01766(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = f'{xml_value}'
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
