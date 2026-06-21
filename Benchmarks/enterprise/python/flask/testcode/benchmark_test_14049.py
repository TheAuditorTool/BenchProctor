# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import requests


def BenchmarkTest14049():
    user_id = request.args.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = asyncio.run(fetch_payload())
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
