# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from fastapi import Form
from starlette.responses import JSONResponse
import os


async def BenchmarkTest35427(request: Request, field: str = Form('')):
    field_value = field
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(field_value).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
