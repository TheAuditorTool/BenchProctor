# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import json
import os


async def BenchmarkTest05777(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    try:
        data = json.loads(dotenv_value).get('value', dotenv_value)
    except (json.JSONDecodeError, AttributeError):
        data = dotenv_value
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
