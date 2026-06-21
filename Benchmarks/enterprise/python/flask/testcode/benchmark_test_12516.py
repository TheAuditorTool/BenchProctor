# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify
import time
import asyncio
from app_runtime import db


def BenchmarkTest12516():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
