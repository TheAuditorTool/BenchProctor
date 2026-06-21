# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import asyncio
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest05880():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    async def _evasion_task():
        os.system('echo ' + str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
