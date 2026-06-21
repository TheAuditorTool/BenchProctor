# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from starlette.responses import JSONResponse
import os


async def BenchmarkTest72550(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(header_value).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
