# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from cryptography.fernet import Fernet
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest46280(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = handle(config_value)
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode()).decode()
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', encrypted, secure=True, httponly=True, samesite='Strict')
    return resp
