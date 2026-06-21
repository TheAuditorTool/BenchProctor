# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import importlib


def BenchmarkTest43972():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = asyncio.run(fetch_payload())
    def _primary():
        importlib.import_module(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
