# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os
import json


async def BenchmarkTest65005(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return {"updated": True}
