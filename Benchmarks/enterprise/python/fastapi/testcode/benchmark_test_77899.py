# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from urllib.parse import unquote
from fastapi import Form
from starlette.responses import JSONResponse
import os


async def BenchmarkTest77899(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
