# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from starlette.responses import JSONResponse
import os
from app_runtime import db


def normalise_input(value):
    return value.strip()

async def BenchmarkTest01800(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = normalise_input(db_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
