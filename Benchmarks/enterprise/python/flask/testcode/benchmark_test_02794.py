# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
from app_runtime import db


def BenchmarkTest02794():
    host_value = request.headers.get('Host', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return host_value
    data = asyncio.run(fetch_payload())
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return jsonify({"result": "success"})
