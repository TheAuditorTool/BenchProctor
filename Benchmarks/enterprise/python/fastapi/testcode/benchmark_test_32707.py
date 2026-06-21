# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest32707(request: Request):
    secret_value = 'app_display_name'
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(secret_value).encode())
    return {"updated": True}
