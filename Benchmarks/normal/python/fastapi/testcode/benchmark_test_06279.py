# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


request_state: dict[str, str] = {}

async def BenchmarkTest06279(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
