# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import asyncio
from types import SimpleNamespace


def BenchmarkTest53860():
    ua_value = request.headers.get('User-Agent', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
