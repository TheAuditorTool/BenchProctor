# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest03737(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    Fernet(dotenv_value.encode() if isinstance(dotenv_value, str) else dotenv_value).encrypt(b'data')
    return {"updated": True}
