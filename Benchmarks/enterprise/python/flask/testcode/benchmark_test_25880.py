# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import asyncio


def BenchmarkTest25880(path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    requests.post('http://api.prod.internal/data', data=str(processed))
    return jsonify({"result": "success"})
