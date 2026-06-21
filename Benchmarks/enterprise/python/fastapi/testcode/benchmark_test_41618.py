# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from starlette.responses import JSONResponse
import os


def to_text(value):
    return str(value).strip()

async def BenchmarkTest41618(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = to_text(cookie_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
