# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
from types import SimpleNamespace


def BenchmarkTest49747():
    raw_body = request.get_data(as_text=True)
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        eval(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
