# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
from types import SimpleNamespace


def BenchmarkTest24847():
    cookie_value = request.cookies.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        eval(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
