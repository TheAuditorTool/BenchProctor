# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import asyncio
from app_runtime import db


def BenchmarkTest21587():
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return jsonify({'record': str(record)}), 200
