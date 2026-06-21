# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from cryptography.fernet import Fernet
from flask import jsonify
import os
import asyncio


def BenchmarkTest01397():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    async def fetch_payload():
        await asyncio.sleep(0)
        return config_value
    data = asyncio.run(fetch_payload())
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode()).decode()
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', encrypted, secure=True, httponly=True, samesite='Strict')
    return resp
