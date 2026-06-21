# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import asyncio
from app_runtime import db


def BenchmarkTest41240():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(db_value)
    data = collected
    async def _evasion_task():
        db.users.find({'$where': "this.username == '" + str(data) + "'"})
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
