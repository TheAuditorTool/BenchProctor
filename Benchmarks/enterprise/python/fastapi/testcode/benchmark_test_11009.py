# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from cryptography.fernet import Fernet
import os


async def BenchmarkTest11009(request: Request):
    path_value = request.path_params.get('id', '')
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(path_value).encode()).decode()
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', encrypted, secure=True, httponly=True, samesite='Strict')
    return resp
