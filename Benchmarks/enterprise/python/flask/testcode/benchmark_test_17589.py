# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import asyncio


def BenchmarkTest17589():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
