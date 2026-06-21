# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from cryptography.fernet import Fernet
import json
import os
from types import SimpleNamespace


async def BenchmarkTest81406(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode()).decode()
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', encrypted, secure=True, httponly=True, samesite='Strict')
    return resp
