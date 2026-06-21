# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from starlette.responses import JSONResponse
import os


async def BenchmarkTest12659(request: Request):
    auth_header = request.headers.get('authorization', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(auth_header).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
