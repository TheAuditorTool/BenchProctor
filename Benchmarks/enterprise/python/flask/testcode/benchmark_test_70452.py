# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
from types import SimpleNamespace


def BenchmarkTest70452():
    origin_value = request.headers.get('Origin', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        with open('/var/app/data/' + str(data), 'w') as fh:
            fh.write('data')
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
