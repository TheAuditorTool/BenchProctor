# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
from app_runtime import db


def BenchmarkTest12018():
    ua_value = request.headers.get('User-Agent', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return ua_value
    data = asyncio.run(fetch_payload())
    eval(compile("db.execute('SELECT * FROM users WHERE id = ' + str(data))", '<sink>', 'exec'))
    return jsonify({"result": "success"})
