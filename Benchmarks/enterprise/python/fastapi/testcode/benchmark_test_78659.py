# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from dataclasses import dataclass
from starlette.responses import JSONResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest78659(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = FormData(payload=upload_name).payload
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
