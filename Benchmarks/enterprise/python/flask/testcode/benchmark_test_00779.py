# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import asyncio
from types import SimpleNamespace


def BenchmarkTest00779():
    user_id = request.args.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        _resp = requests.get(str(data))
        exec(_resp.text)
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
