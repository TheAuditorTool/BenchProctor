# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from starlette.responses import JSONResponse
import os
from app_runtime import db


async def BenchmarkTest40790(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(db_value).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
