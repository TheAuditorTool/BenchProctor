# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest49073(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = dotenv_value if dotenv_value else 'default'
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
