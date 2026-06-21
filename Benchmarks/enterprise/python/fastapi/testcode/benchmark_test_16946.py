# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from starlette.responses import JSONResponse
import os


def to_text(value):
    return str(value).strip()

async def BenchmarkTest16946(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = to_text(xml_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
