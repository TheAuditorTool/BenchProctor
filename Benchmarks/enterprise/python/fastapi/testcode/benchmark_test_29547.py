# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from starlette.responses import JSONResponse
import os


async def BenchmarkTest29547(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(xml_value).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
