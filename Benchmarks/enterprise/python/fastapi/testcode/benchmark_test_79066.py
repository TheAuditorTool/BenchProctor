# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest79066(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    if dotenv_value:
        data = dotenv_value
    else:
        data = ''
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
