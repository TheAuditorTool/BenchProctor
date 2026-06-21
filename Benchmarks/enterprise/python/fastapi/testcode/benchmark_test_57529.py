# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from starlette.responses import JSONResponse
import os


async def BenchmarkTest57529(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(forwarded_ip).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
