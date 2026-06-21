# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import asyncio
from app_runtime import db


def BenchmarkTest07119():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return profile_value
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    os.unlink('/var/app/data/' + str(processed))
    return jsonify({"result": "success"})
