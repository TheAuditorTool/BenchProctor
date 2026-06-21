# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os
from starlette.responses import JSONResponse


async def BenchmarkTest61267(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(env_value).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
