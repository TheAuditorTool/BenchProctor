# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
import asyncio
from app_runtime import db


def BenchmarkTest55579(path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    if os.environ.get("APP_ENV", "production") != "test":
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return jsonify({"result": "success"})
