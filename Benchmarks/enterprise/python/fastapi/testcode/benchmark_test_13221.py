# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from starlette.responses import JSONResponse
import os


def ensure_str(value):
    return str(value)

async def BenchmarkTest13221(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = ensure_str(upload_name)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
