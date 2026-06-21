# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


def to_text(value):
    return str(value).strip()

def BenchmarkTest18032():
    ua_value = request.headers.get('User-Agent', '')
    data = to_text(ua_value)
    async def _evasion_task():
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
