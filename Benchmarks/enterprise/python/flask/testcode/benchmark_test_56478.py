# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import asyncio
from app_runtime import auth_check


def BenchmarkTest56478():
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    auth_check('user', data)
    return jsonify({"result": "success"})
