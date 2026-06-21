# SPDX-License-Identifier: Apache-2.0
from flask import request
import asyncio


def BenchmarkTest78812():
    ua_value = request.headers.get('User-Agent', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return ua_value
    data = asyncio.run(fetch_payload())
    return str(data), 200, {'Content-Type': 'text/html'}
