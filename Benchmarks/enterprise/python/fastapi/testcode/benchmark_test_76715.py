# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


request_state: dict[str, str] = {}

async def BenchmarkTest76715(request: Request):
    secret_value = 'feature_flag_value'
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return {"updated": True}
