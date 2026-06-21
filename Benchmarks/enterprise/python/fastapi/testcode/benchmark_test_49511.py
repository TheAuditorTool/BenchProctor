# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from starlette.responses import JSONResponse
import os


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest49511(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = default_blank(forwarded_ip)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
