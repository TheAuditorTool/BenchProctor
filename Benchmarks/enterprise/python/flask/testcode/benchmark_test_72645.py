# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
from app_runtime import db


def BenchmarkTest72645():
    raw_body = request.get_data(as_text=True)
    async def fetch_payload():
        await asyncio.sleep(0)
        return raw_body
    data = asyncio.run(fetch_payload())
    def _primary():
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
