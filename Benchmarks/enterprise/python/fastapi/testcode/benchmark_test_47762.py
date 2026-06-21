# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest47762(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    Fernet(env_value.encode() if isinstance(env_value, str) else env_value).encrypt(b'data')
    return {"updated": True}
