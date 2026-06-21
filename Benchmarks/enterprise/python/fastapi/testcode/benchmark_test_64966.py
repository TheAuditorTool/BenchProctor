# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from dataclasses import dataclass
from starlette.responses import JSONResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest64966(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
