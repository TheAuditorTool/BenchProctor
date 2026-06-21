# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import socket


def BenchmarkTest54344():
    referer_value = request.headers.get('Referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = asyncio.run(fetch_payload())
    def _primary():
        s = socket.create_connection((str(data), 80))
        s.close()
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
