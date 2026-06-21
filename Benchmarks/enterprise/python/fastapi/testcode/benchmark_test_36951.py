# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import re
from starlette.responses import JSONResponse


request_state: dict[str, str] = {}

async def BenchmarkTest36951(request: Request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    Fernet(processed.encode() if isinstance(processed, str) else processed).encrypt(b'data')
    return {"updated": True}
