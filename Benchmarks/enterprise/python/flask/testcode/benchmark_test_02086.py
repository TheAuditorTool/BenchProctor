# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import asyncio
import defusedxml.ElementTree
from app_runtime import db


def BenchmarkTest02086():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = asyncio.run(fetch_payload())
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
