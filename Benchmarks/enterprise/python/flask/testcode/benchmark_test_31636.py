# SPDX-License-Identifier: Apache-2.0
from flask import request
import asyncio


def BenchmarkTest31636():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = asyncio.run(fetch_payload())
    return str(data), 200, {'Content-Type': 'text/html'}
