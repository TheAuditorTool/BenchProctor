# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest50265(request: Request):
    secret_value = 'default_setting_value'
    parts = []
    for token in str(secret_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return {"updated": True}
