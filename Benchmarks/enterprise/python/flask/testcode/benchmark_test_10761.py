# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


def BenchmarkTest10761():
    referer_value = request.headers.get('Referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = asyncio.run(fetch_payload())
    async def _evasion_task():
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
