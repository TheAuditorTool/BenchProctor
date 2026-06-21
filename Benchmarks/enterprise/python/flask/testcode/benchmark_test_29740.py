# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import asyncio
from app_runtime import auth_check


def BenchmarkTest29740():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    async def fetch_payload():
        await asyncio.sleep(0)
        return file_value
    data = asyncio.run(fetch_payload())
    auth_check('user', data)
    return jsonify({"result": "success"})
