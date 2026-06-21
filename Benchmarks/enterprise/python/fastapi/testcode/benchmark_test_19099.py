# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from starlette.responses import JSONResponse
import os


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest19099(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = coalesce_blank(raw_body)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
