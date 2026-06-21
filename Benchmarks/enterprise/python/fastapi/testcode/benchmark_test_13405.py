# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from starlette.responses import JSONResponse
import os


async def BenchmarkTest13405(request: Request):
    referer_value = request.headers.get('referer', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(referer_value).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
