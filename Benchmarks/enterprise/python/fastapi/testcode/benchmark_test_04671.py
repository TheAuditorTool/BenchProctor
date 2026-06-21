# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from starlette.responses import JSONResponse
import os


async def BenchmarkTest04671(request: Request):
    ua_value = request.headers.get('user-agent', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(ua_value).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
