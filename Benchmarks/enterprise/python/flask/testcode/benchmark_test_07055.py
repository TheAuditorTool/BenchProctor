# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import asyncio


def BenchmarkTest07055():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = asyncio.run(fetch_payload())
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
