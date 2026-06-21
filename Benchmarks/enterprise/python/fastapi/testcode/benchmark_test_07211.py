# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest07211(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = dotenv_value if dotenv_value else 'default'
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return {"updated": True}
