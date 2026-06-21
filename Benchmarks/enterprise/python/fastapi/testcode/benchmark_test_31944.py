# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from fastapi import Form
from starlette.responses import JSONResponse
import os


def normalise_input(value):
    return value.strip()

async def BenchmarkTest31944(request: Request, field: str = Form('')):
    field_value = field
    data = normalise_input(field_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
