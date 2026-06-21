# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


def normalise_input(value):
    return value.strip()

def BenchmarkTest33438():
    raw_body = request.get_data(as_text=True)
    data = normalise_input(raw_body)
    async def _evasion_task():
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
