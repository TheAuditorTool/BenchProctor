# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import asyncio


def BenchmarkTest17689():
    field_value = request.form.get('field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = asyncio.run(fetch_payload())
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
