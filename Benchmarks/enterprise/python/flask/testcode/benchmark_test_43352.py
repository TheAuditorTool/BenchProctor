# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import asyncio


def BenchmarkTest43352():
    ua_value = request.headers.get('User-Agent', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return ua_value
    data = asyncio.run(fetch_payload())
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
