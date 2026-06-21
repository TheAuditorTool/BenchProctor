# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from urllib.parse import unquote
import os


async def BenchmarkTest08648(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    key = os.environ['DATA_ENC_KEY'].encode()
    with open('/var/www/html/exports/report.txt', 'wb') as fh:
        fh.write(Fernet(key).encrypt(str(data).encode()))
    return {"updated": True}
