# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import asyncio
from app_runtime import db


def BenchmarkTest43768():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = asyncio.run(fetch_payload())
    eval(compile("os.unlink('/var/app/data/' + str(data))", '<sink>', 'exec'))
    return jsonify({"result": "success"})
