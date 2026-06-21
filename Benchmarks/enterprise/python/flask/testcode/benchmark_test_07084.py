# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import os
import asyncio
from app_runtime import db


def BenchmarkTest07084():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = asyncio.run(fetch_payload())
    key = os.environ['DATA_ENC_KEY'].encode()
    globals().setdefault('_secret_cache', {})['current'] = Fernet(key).encrypt(str(data).encode())
    return jsonify({"result": "success"})
