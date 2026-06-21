# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest33092(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
