# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from starlette.responses import JSONResponse
import os
from app_runtime import db


async def BenchmarkTest60765(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(comment_value).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
