# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest78396(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(dotenv_value).encode())
    return {"updated": True}
