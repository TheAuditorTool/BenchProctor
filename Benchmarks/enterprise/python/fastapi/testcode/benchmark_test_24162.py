# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest24162(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
