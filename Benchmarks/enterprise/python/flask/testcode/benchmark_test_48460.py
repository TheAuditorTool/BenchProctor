# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
from app_runtime import db


def BenchmarkTest48460():
    multipart_value = request.form.get('multipart_field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return multipart_value
    data = asyncio.run(fetch_payload())
    async def _evasion_task():
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
