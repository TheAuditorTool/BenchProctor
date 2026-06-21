# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest26408(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data, _sep, _rest = str(dotenv_value).partition('\x00')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
