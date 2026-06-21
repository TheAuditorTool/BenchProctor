# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify
import asyncio


def BenchmarkTest75609():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = asyncio.run(fetch_payload())
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200
