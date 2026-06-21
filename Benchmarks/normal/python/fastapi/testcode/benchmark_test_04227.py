# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from starlette.responses import JSONResponse
import os


async def BenchmarkTest04227(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
