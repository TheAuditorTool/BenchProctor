# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from starlette.responses import JSONResponse
import os


async def BenchmarkTest06443(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(multipart_value).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
