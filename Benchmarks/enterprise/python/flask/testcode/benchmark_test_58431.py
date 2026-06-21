# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
from app_runtime import db


def BenchmarkTest58431():
    auth_header = request.headers.get('Authorization', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    db.users.find({'$where': "this.username == '" + str(processed) + "'"})
    return jsonify({"result": "success"})
