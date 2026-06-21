# SPDX-License-Identifier: Apache-2.0
from flask import request
import asyncio


def BenchmarkTest00072():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    return str(data), 200, {'Content-Type': 'text/html'}
