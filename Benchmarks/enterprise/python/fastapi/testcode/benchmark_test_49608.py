# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from starlette.responses import JSONResponse
import os


def normalise_input(value):
    return value.strip()

async def BenchmarkTest49608(request: Request):
    host_value = request.headers.get('host', '')
    data = normalise_input(host_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
