# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest08524(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Access-Control-Allow-Origin': str(data)})
