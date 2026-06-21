# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import os
import asyncio


def BenchmarkTest07058():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return dotenv_value
    data = asyncio.run(fetch_payload())
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
