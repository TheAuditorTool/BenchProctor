# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from starlette.responses import JSONResponse
import os


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest16067(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = default_blank(cookie_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
