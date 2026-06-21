# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
from app_runtime import db


def BenchmarkTest62076():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return jsonify({"result": "success"})
