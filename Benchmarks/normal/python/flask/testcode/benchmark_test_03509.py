# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import asyncio


def BenchmarkTest03509():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    async def fetch_payload():
        await asyncio.sleep(0)
        return secret_value
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(processed)})
    return jsonify({"result": "success"})
