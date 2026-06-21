# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt


request_state: dict[str, str] = {}

async def BenchmarkTest71800(request: Request):
    secret_value = 'config_secret_test_abc123'
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    processed = data[:64]
    jwt.encode({'sub': 'user'}, processed, algorithm='HS256')
    return {"updated": True}
