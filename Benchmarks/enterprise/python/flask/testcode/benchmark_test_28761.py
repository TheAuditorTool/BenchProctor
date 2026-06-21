# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import socket


def BenchmarkTest28761():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    async def _evasion_task():
        s = socket.create_connection((str(data), 80))
        s.close()
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
