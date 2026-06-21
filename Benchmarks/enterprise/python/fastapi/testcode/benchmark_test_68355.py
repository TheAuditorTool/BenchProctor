# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from dataclasses import dataclass
from starlette.responses import JSONResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest68355(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
