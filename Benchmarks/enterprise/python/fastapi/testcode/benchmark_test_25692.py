# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from starlette.responses import JSONResponse
import os


async def BenchmarkTest25692(request: Request):
    path_value = request.path_params.get('id', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(path_value).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
