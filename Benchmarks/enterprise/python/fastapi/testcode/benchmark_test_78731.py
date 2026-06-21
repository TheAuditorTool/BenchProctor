# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest78731(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(env_value).encode())
    return {"updated": True}
