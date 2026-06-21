# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import asyncio


def BenchmarkTest40602():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    async def fetch_payload():
        await asyncio.sleep(0)
        return prop_value
    data = asyncio.run(fetch_payload())
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
