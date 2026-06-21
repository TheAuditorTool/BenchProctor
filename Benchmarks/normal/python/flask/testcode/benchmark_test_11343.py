# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import asyncio
from app_runtime import db


def BenchmarkTest11343():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = asyncio.run(fetch_payload())
    async def _evasion_task():
        os.unlink('/var/app/data/' + str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
